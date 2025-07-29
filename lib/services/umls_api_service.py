"""
UMLS API Service.
"""
import logging
import time
from functools import lru_cache
from typing import Dict, List, Optional, Union

import requests

#INTERVAL = 0.05 # 20 requests per second
COURTESY_PADDING = 0.005
INTERVAL = 0.05 + COURTESY_PADDING # 20 requests per second with padding


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

    def search_concept(
        self,
        term: Optional[Union[str, int]],
        sabs: Optional[List[str]] = None,
        search_type: str = "words",
        return_id_type: str = "concept",
    ) -> Optional[Dict[str, Optional[Union[str, int]]]]:
        """
        Search UMLS for a given string and return top matching concept info.
        """

        params = {
            "string": term,
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
        response = self.session.get(
            f"{self.base_url}/rest/content/current/CUI/{cui}/atoms",
            params={"apiKey": self.api_key},
        )

        time.sleep(INTERVAL)

        if response.status_code != 200:
            logging.warning(f"Failed to get atoms for CUI {cui}")
            return []

        return response.json().get("result", [])

    def normalize_entities(
        self,
        entities: List[Dict[str, Optional[Union[str, int]]]],
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

    def get_icd10cm_from_cui(self, cui: str) -> List[Dict[str, Optional[Union[str, int]]]]:
        """
        Return all ICD-10-CM codes mapped from a given UMLS CUI.
        """
        response = self.session.get(
            f"{self.base_url}/rest/crosswalk/current/source/UMLS/{cui}",
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

@lru_cache(maxsize=4096)
def normalize(umls: UMLSApiService, text: str) -> Optional[Dict[str, Optional[Union[str, int]]]]:
    """
    Normalize a given text using UMLS API.
    :param text: str - The text to normalize.
    :return: Optional[Dict[str, Optional[Union[str, int]]]] - A dictionary with 'cui', 'name', and 'score' if found, else None.
    """
    return umls.search_concept(text)
