"""
APIs for fetching medical data from various sources like Medline, ClinicalTrials, and NCBI.
"""
import time
from typing import List

import requests

from lib.logger import Logger
from settings import logger

icd10_codes = {
    'asthma': 'J45.40',
    'diabetes (type 2)': 'E11.9',
}
# https://connect.medlineplus.gov/service?knowledgeResponseType=application%2Fjson&mainSearchCriteria.v.cs=2.16.840.1.113883.6.90&mainSearchCriteria.v.c={icd10_code}&mainSearchCriteria.v.dn=&informationRecipient.languageCode.c=en

class ICD10Code(str):
    """
    Custom ICD10Code type for better type safety.
    Inherits from str to allow direct string usage.

    Format: `ICD10:{icd10_code}`
    """
    def validate(self) -> bool:
        """
        Validates the ICD-10 code format.
        :return: True if valid, False otherwise.
        """
        # Simple validation for ICD-10 code format
        return bool(self and len(self) >= 3 and self[0].isalpha() and self[1:].isdigit())


class Medline:
    """
    Fetches medical information from Medline using ICD-10 codes.
    """
    def __init__(self, logger: Logger) -> None:
        """
        Initializes the Medline class with a logger.
        :param logger: Logger instance for logging errors and information.
        :return: None
        """
        self.logger = logger

    def fetch_medline(self, icd10_code: ICD10Code) -> dict:
        """
        https://connect.medlineplus.gov/service?

        knowledgeResponseType=application%2Fjson
            &mainSearchCriteria.v.cs=2.16.840.1.113883.6.90
            &mainSearchCriteria.v.c={icd10_code}
            &mainSearchCriteria.v.dn=
            &informationRecipient.languageCode.c=en

        Fetches medical information from Medline using the provided ICD-10 code.
        :param icd10_code: The ICD-10 code for the medical condition.
        :return: A dictionary containing the medical information or an error message.
        """
        if not icd10_code.validate():
            self.logger.error(f"Invalid ICD-10 code format: {icd10_code}")
            return {"error": "Invalid ICD-10 code format"}

        url = f"https://connect.medlineplus.gov/service?knowledgeResponseType=application%2Fjson&mainSearchCriteria.v.cs=2.16.840.1.113883.6.90&mainSearchCriteria.v.c={icd10_code}&mainSearchCriteria.v.dn=&informationRecipient.languageCode.c=en"
        headers = {
            "accept": "application/json"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            self.logger.error(f"Error fetching Medline data: {response.status_code} - {response.text}")
            return {"error": "Failed to fetch Medline data"}



class ClinicalTrials:
    """
    Fetches clinical trial data from ClinicalTrials.gov.
    """
    def __init__(self, logger: Logger) -> None:
        """
        Initializes the ClinicalTrials class with a logger.
        :param logger: Logger instance for logging errors and information.
        :return: None
        """
        self.logger = logger

    def fetch_clinical_trials(self, query: str) -> dict:
        """
        Fetches clinical trial data from ClinicalTrials.gov based on the provided query.

        curl -X GET "https://clinicaltrials.gov/api/v2/studies" -H "accept: application/json"

        :param query: The search query for clinical trials.
        :return: A dictionary containing the clinical trial data or an error message.
        """
        import requests
        url = "https://clinicaltrials.gov/api/v2/studies"

        headers = {
            "accept": "application/json"
        }

        data = {
            "query.cond": query
        }

        response = requests.get(
            url,
            params=data,
            headers=headers
        )

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            self.logger.error(f"Error fetching clinical trials: {response.status_code} - {response.text}")
            return {"error": "Failed to fetch clinical trials"}


class NCBI:
    """
    Fetches medical studies and articles from NCBI's PubMed database.
    Uses the Entrez API to search for articles based on a query.
    """
    def __init__(self, email: str, logger: Logger, api_key: str) -> None:
        """
        Initializes the NCBI class with email, logger, and API key.
        :param email: Email address for user calling API.
        :param logger: Logger instance for logging errors and information.
        :param api_key: NCBI API key for authentication.
        :return: None
        """
        self.email = email
        self.logger = logger
        self.api_key = api_key

        self.BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
        self.HEADERS = {
            # Good etiquette: identify your tool and give a contact e-mail
            "User-Agent": f"arsmedicatech/0.1 ({self.email})"
        }

    def fetch_ncbi_studies(self, query: str, debug: bool = False) -> list:
        """
        Fetches studies from NCBI's PubMed database based on the provided query.
        :param query: The search query for PubMed articles.
        :param debug: If True, logs detailed information about the search results.
        :return: A list of dictionaries containing article information.
        """
        hits, total_found = self.search_pubmed(query, max_records=10, with_abstract=True)
        if debug:
            logger.debug(f"{total_found:,} articles in PubMed; showing {len(hits)} results:\n")
            for i, art in enumerate(hits, 1):
                logger.debug(f"{i}. {art['title']}  ({art['journal']}, {art['pubdate']})")
                logger.debug(f"   PMID: {art['pmid']}")
                logger.debug(f"   Authors: {art['authors']}")
                if 'abstract' in art:
                    logger.debug(f"   Abstract (truncated): {art['abstract'][:300]}...\n")
        return hits

    def esearch(self, query: str, retmax: int = 100) -> tuple:
        """
        Return up to retmax PubMed IDs (PMIDs) that match the query.

        Uses the Entrez ESearch API to search for articles in PubMed.
        :param query: The search query for PubMed articles.
        :param retmax: Maximum number of results to return.
        :return: A tuple containing a list of PMIDs and the total number of hits.
        """
        params = {
            "db": "pubmed",
            "term": query,
            "retmode": "json",
            "retmax": retmax,
            "sort": "relevance",
            "api_key": self.api_key,
            "tool": "clinical-search",
            "email": self.email
        }
        r = requests.get(self.BASE + "esearch.fcgi", params=params, headers=self.HEADERS, timeout=15)
        r.raise_for_status()
        data = r.json()["esearchresult"]
        return data["idlist"], int(data["count"])  # (list of PMIDs, total hits)

    def esummary(self, pmids: List[str]) -> dict:
        """
        Return a dict keyed by PMID with title, journal, authors, pubdate, etc.

        Uses the Entrez ESummary API to fetch article summaries from PubMed.
        :param pmids: List of PubMed IDs (PMIDs) to fetch summaries for.
        :return: A dictionary where keys are PMIDs and values are article summaries.
        """
        if not pmids:
            return {}
        params = {
            "db": "pubmed",
            "id": ",".join(pmids),
            "retmode": "json",
            "api_key": self.api_key,
            "tool": "clinical-search",
            "email": self.email
        }
        r = requests.get(self.BASE + "esummary.fcgi", params=params, headers=self.HEADERS, timeout=15)
        r.raise_for_status()
        summaries = r.json()["result"]
        # The JSON has a useless 'uids' list; filter it out
        return {pmid: summaries[pmid] for pmid in summaries if pmid != "uids"}

    def efetch_abstract(self, pmid: str) -> str:
        """
        Return the plain-text abstract for one PMID (or '' if none).

        Uses the Entrez EFetch API to fetch the abstract of a PubMed article.
        :param pmid: The PubMed ID (PMID) of the article to fetch the abstract for.
        :return: The abstract text of the article, or an empty string if not found.
        """
        params = {
            "db": "pubmed",
            "id": pmid,
            "rettype": "abstract",
            "retmode": "text",
            "api_key": self.api_key,
            "tool": "clinical-search",
            "email": self.email
        }
        r = requests.get(self.BASE + "efetch.fcgi", params=params, headers=self.HEADERS, timeout=15)
        r.raise_for_status()
        return r.text.strip()

    def search_pubmed(self, query: str, max_records: int = 20, with_abstract: bool = False, delay: float = 0.35) -> tuple:
        """
        High-level helper.
        Returns a list of dicts: [{pmid, title, journal, authors, pubdate, abstract?}, ...]

        Uses the Entrez ESearch and ESummary APIs to search for articles in PubMed.
        :param query: The search query for PubMed articles.
        :param max_records: Maximum number of records to return.
        :param with_abstract: If True, fetches the abstract for each article.
        :param delay: Delay in seconds between requests to avoid hitting the rate limit.
        :return: A tuple containing a list of dictionaries with article information and the total number of hits.
        """
        ids, total = self.esearch(query, retmax=max_records)
        summaries = self.esummary(ids)

        results = []
        for pmid in ids:
            doc = summaries[pmid]
            item = {
                "pmid": pmid,
                "title": doc["title"],
                "journal": doc["fulljournalname"],
                "pubdate": doc["pubdate"],
                "authors": ", ".join(a["name"] for a in doc.get("authors", [])[:5]),
            }
            if with_abstract:
                # Courtesy pause to avoid hitting the rate limit
                time.sleep(delay)
                item["abstract"] = self.efetch_abstract(pmid)
            results.append(item)
        return results, total
