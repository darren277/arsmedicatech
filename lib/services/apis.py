""""""
import time
import requests

icd10_codes = {
    'asthma': 'J45.40',
    'diabetes (type 2)': 'E11.9',
}
# https://connect.medlineplus.gov/service?knowledgeResponseType=application%2Fjson&mainSearchCriteria.v.cs=2.16.840.1.113883.6.90&mainSearchCriteria.v.c={icd10_code}&mainSearchCriteria.v.dn=&informationRecipient.languageCode.c=en


class Medline:
    def __init__(self, logger):
        self.logger = logger

    def fetch_medline(self, icd10_code: str):
        """
        https://connect.medlineplus.gov/service?

        knowledgeResponseType=application%2Fjson
            &mainSearchCriteria.v.cs=2.16.840.1.113883.6.90
            &mainSearchCriteria.v.c={icd10_code}
            &mainSearchCriteria.v.dn=
            &informationRecipient.languageCode.c=en

        :return:
        """
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
    def __init__(self, logger):
        self.logger = logger

    def fetch_clinical_trials(self, query: str):
        """
        curl -X GET "https://clinicaltrials.gov/api/v2/studies" -H "accept: application/json"
        :return:
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
    def __init__(self, email: str, logger, api_key: str):
        self.email = email
        self.logger = logger
        self.api_key = api_key

        self.BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
        self.HEADERS = {
            # Good etiquette: identify your tool and give a contact e-mail
            "User-Agent": f"arsmedicatech/0.1 ({self.email})"
        }

    def fetch_ncbi_studies(self, query: str, debug: bool = False):
        hits, total_found = self.search_pubmed(query, max_records=10, with_abstract=True)
        if debug:
            print(f"{total_found:,} articles in PubMed; showing {len(hits)} results:\n")
            for i, art in enumerate(hits, 1):
                print(f"{i}. {art['title']}  ({art['journal']}, {art['pubdate']})")
                print(f"   PMID: {art['pmid']}")
                print(f"   Authors: {art['authors']}")
                if 'abstract' in art:
                    print(f"   Abstract (truncated): {art['abstract'][:300]}...\n")
        return hits

    def esearch(self, query, retmax=100):
        """Return up to retmax PubMed IDs (PMIDs) that match the query."""
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

    def esummary(self, pmids):
        """Return a dict keyed by PMID with title, journal, authors, pubdate, etc."""
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

    def efetch_abstract(self, pmid):
        """Return the plain-text abstract for one PMID (or '' if none)."""
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

    def search_pubmed(self, query, max_records=20, with_abstract=False, delay=0.35):
        """
        High-level helper.
        Returns a list of dicts: [{pmid, title, journal, authors, pubdate, abstract?}, ...]
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
