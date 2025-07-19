"""
ICD Autocoder Service.
"""
from typing import List, TypedDict, Dict

from settings import UMLS_API_KEY
from umls_api_service import UMLSApiService


class Entity(TypedDict):
    """
    Represents a named entity extracted from text.
    """
    text: str
    label: str
    start_char: int
    end_char: int


class ICDAutoCoderService:
    """
    A service for extracting named entities from text using an external NER API and then normalizing them using UMLS.
    The service also performs ICD code matching.
    """
    def __init__(self, text: str) -> None:
        self.text = text

        self.umls_service = UMLSApiService(api_key=UMLS_API_KEY)

    def ner_concept_extraction(self, text: str) -> List[Entity]:
        """
        Extract named entities from the provided text.

        curl -X POST https://demo.arsmedicatech.com/ner/extract -H "Content-Type: application/json" -d '{"text":"Patient presents with Type 2 diabetes mellitus and essential hypertension."}'

        Returns: {"entities":[{"text":"Patient","label":"ENTITY","start_char":0,"end_char":7},{"text":"Type 2 diabetes mellitus","label":"ENTITY","start_char":22,"end_char":46},{"text":"essential hypertension","label":"ENTITY","start_char":51,"end_char":73}]}
        """
        import requests

        url = "https://demo.arsmedicatech.com/ner/extract"
        headers = {"Content-Type": "application/json"}
        payload = {"text": text}

        response = requests.post(url, json=payload, headers=headers)
        if response.status_code != 200:
            raise RuntimeError(f"NER extraction failed: {response.text}")

        data = response.json()
        entities = data.get("entities", [])
        if not entities:
            raise ValueError("No entities found in the response.")

        ner_output = [
            Entity(
                text=entity["text"],
                label=entity["label"],
                start_char=entity["start_char"],
                end_char=entity["end_char"]
            )
            for entity in entities
        ]

        return ner_output

    def normalize_entities(self, ner_entities: List[Entity]) -> List[Entity]:
        """
        Normalize entities using UMLS API.

        Returns a list of normalized entities.
        """
        normalized_entities = []

        normalized = self.umls_service.normalize_entities(ner_entities)

        for entry in normalized:
            print(entry)

        return normalized_entities

    def match_icd_codes(self, normalized_entities: List[Entity]) -> List[Dict[str, str]]:
        """
        Match ICD-10-CM codes to normalized entities using UMLS API.
        This method updates the entities with ICD-10-CM codes if available.
        :param normalized_entities: List of normalized entities with 'cui' field.
        :return: List of entities with matched ICD-10-CM codes.
        """
        for entity in normalized_entities:
            print("Processing entity:", entity)
            if entity.get("cui"):
                icd_matches = self.umls_service.get_icd10cm_from_cui(entity["cui"])
                if icd_matches:
                    # Pick first match (or apply ranking/scoring logic)
                    entity["icd10cm"] = icd_matches[0]["code"]
                    entity["icd10cm_name"] = icd_matches[0]["name"]
                else:
                    entity["icd10cm"] = None
                    entity["icd10cm_name"] = None

    def main(self) -> Dict[str, List[Entity]]:
        """
        Main method to run the service.
        """
        # Step 1: Extract entities from text
        entities = self.ner_concept_extraction(self.text)
        print("Extracted Entities:", entities)

        # Step 2: Normalize entities using UMLS
        normalized_entities = self.normalize_entities(entities)
        print("Normalized Entities:", normalized_entities)

        # Step 3: Match ICD codes (not implemented yet)
        icd_codes = self.match_icd_codes(normalized_entities)
        print("Matched ICD Codes:", icd_codes)

        return dict(
            entities=entities,
            normalized_entities=normalized_entities,
            icd_codes=icd_codes
        )

