"""
UMLS API Service.
"""
import requests
from typing import Optional, List, Dict
import logging
import time
from functools import lru_cache

#INTERVAL = 0.05 # 20 requests per second
COURTESY_PADDING = 0.005
INTERVAL = 0.05 + COURTESY_PADDING # 20 requests per second with padding

@lru_cache(maxsize=4096)
def normalize(text) -> Optional[Dict[str, str]]:
    """
    Normalize a given text using UMLS API.
    :param text: str - The text to normalize.
    :return: Optional[Dict[str, str]] - A dictionary with 'cui', 'name', and 'score' if found, else None.
    """
    return umls.search_concept(text)


class UMLSApiService:
    """
    A wrapper for interacting with the UMLS REST API.
    Handles TGT/ST authentication, concept search, and normalization.

    ToS:
    "In order to avoid overloading our servers, NLM requires that users send no more than 20 requests per second per IP address."
    "To limit the number of requests that you send to the APIs, NLM recommends caching results for a 12-24 hour period."
    """

    def __init__(self, api_key: str, base_url: str = "https://uts-ws.nlm.nih.gov"):
        self.api_key = api_key
        self.base_url = base_url
        self.session = requests.Session()
        self.tgt = None
        self.last_auth_time = 0
        self.auth_interval = 8 * 60  # TGT expires every ~8 minutes

    def _authenticate(self):
        """
        Obtain a TGT (ticket-granting ticket) for session reuse.
        """
        auth_url = f"{self.base_url}/restful/isValidServiceTicket"
        tgt_url = f"{self.base_url}/cas/v1/apiKey"

        response = self.session.post(
            tgt_url,
            data={"apikey": self.api_key},
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )

        if response.status_code != 201:
            raise RuntimeError("UMLS authentication failed: " + response.text)

        self.tgt = response.headers["location"]
        self.last_auth_time = time.time()

    def _get_service_ticket(self) -> str:
        """
        Request a single-use ST from the TGT.
        """
        if self.tgt is None or (time.time() - self.last_auth_time > self.auth_interval):
            self._authenticate()

        response = self.session.post(
            self.tgt,
            data={"service": f"{self.base_url}/rest"},
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )

        if response.status_code != 200:
            raise RuntimeError("UMLS service ticket retrieval failed: " + response.text)

        return response.text

    def search_concept(
        self,
        term: str,
        sabs: Optional[List[str]] = None,
        search_type: str = "words",
        return_id_type: str = "concept",
    ) -> Optional[Dict[str, str]]:
        """
        Search UMLS for a given string and return top matching concept info.
        """
        #st = self._get_service_ticket()

        params = {
            "string": term,
            #"ticket": st,
            "apiKey": self.api_key,
            "searchType": search_type,
            "returnIdType": return_id_type,
        }

        if sabs:
            params["sabs"] = ",".join(sabs)

        response = self.session.get(f"{self.base_url}/rest/search/current", params=params)

        time.sleep(INTERVAL)

        if response.status_code != 200:
            logging.warning(f"UMLS search failed for '{term}': {response.status_code}")
            return None

        items = response.json().get("result", {}).get("results", [])
        if not items:
            return None

        top = items[0]
        return {
            "term": term,
            "cui": top.get("ui"),
            "name": top.get("name"),
            "score": top.get("score"),
        }

    def get_atoms_for_cui(self, cui: str) -> List[Dict[str, str]]:
        """
        Return all atom names/synonyms for a given CUI.
        """
        #st = self._get_service_ticket()
        response = self.session.get(
            f"{self.base_url}/rest/content/current/CUI/{cui}/atoms",
            #params={"ticket": st},
            params={"apiKey": self.api_key},
        )

        time.sleep(INTERVAL)

        if response.status_code != 200:
            logging.warning(f"Failed to get atoms for CUI {cui}")
            return []

        return response.json().get("result", [])

    def normalize_entities(
        self,
        entities: List[Dict[str, str]],
        sabs: Optional[List[str]] = ["SNOMEDCT_US", "ICD10CM"]
    ) -> List[Dict]:
        """
        Normalize a list of NER entity dicts: {'text': ..., 'label': ..., ...}
        Returns a list with added 'cui' and 'preferred_name' fields.
        """
        results = []
        for ent in entities:
            norm = self.search_concept(ent["text"], sabs=sabs)
            if norm:
                results.append({
                    **ent,
                    "cui": norm["cui"],
                    "preferred_name": norm["name"],
                    "score": norm["score"]
                })
            else:
                results.append({**ent, "cui": None, "preferred_name": None, "score": 0})
        return results

    def get_icd10cm_from_cui(self, cui: str) -> List[Dict[str, str]]:
        """
        Return all ICD-10-CM codes mapped from a given UMLS CUI.
        """
        #st = self._get_service_ticket()
        response = self.session.get(
            f"{self.base_url}/rest/crosswalk/current/source/UMLS/{cui}",
            #params={"ticket": st, "targetSource": "ICD10CM"},
            params={"apiKey": self.api_key, "targetSource": "ICD10CM"},
        )

        time.sleep(INTERVAL)

        if response.status_code != 200:
            logging.warning(f"Failed ICD10CM crosswalk for CUI {cui}")
            return []

        items = response.json().get("result", [])
        return [
            {
                "code": item["ui"],
                "name": item["name"],
                "source": item["rootSource"]
            }
            for item in items
        ]
