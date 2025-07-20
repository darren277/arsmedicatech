"""
ICD Autocoder Service.
"""
from typing import Any, Dict, List, Optional, TypedDict, Union

from lib.services.umls_api_service import UMLSApiService
from settings import UMLS_API_KEY


class Entity(TypedDict, total=False):
    """
    Represents a named entity extracted from text.
    """
    text: str
    label: str
    start_char: int
    end_char: int
    cui: Optional[str]
    icd10cm: Optional[Union[str, int]]
    icd10cm_name: Optional[Union[str, int]]


def deduplicate(entities: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Deduplicate entities based on their text content while preserving position information.
    
    This function keeps the longest version of each unique entity text while preserving
    the original character positions (start_char, end_char) from the first occurrence
    of that entity in the text. This is important for frontend highlighting.
    
    :param entities: List - A list of entities, each with a 'text' attribute and position info.
    :return: List - A list of deduplicated entities, keeping the longest version of each unique text.
    """
    seen: set[str] = set()
    deduped: List[Dict[str, Any]] = []
    
    # Sort by text length (longest first) to keep the most specific version
    # The position information is preserved from the original entity
    for entity in sorted(entities, key=lambda x: -(len(x['text']))):
        key = entity['text'].lower().strip(" .,:;")
        if key not in seen:
            deduped.append(entity)
            seen.add(key)
    return deduped


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
        # Convert List[Entity] to List[Dict[str, Any]] for the UMLS service
        entities_as_dicts = [
            {
                "text": entity["text"],  # type: ignore
                "label": entity["label"],  # type: ignore
                "start_char": entity["start_char"],  # type: ignore
                "end_char": entity["end_char"]  # type: ignore
            }
            for entity in ner_entities
        ]

        normalized: List[Dict[str, Any]] = self.umls_service.normalize_entities(entities_as_dicts)  # type: ignore
        
        normalized_entities = [
            Entity(
                text=str(entity.get("text", "")),
                label=str(entity.get("label", "")),
                start_char=int(entity.get("start_char", 0)),
                end_char=int(entity.get("end_char", 0)),
                cui=entity.get("cui")
            )
            for entity in normalized
        ]

        return normalized_entities

    def match_icd_codes(self, normalized_entities: List[Entity]) -> List[Entity]:
        """
        Match ICD-10-CM codes to normalized entities using UMLS API.
        This method updates the entities with ICD-10-CM codes if available.
        :param normalized_entities: List of normalized entities with 'cui' field.
        :return: List of entities with matched ICD-10-CM codes.
        """
        for entity in normalized_entities:
            print("Processing entity:", entity)
            if entity.get("cui"):  # type: ignore
                icd_matches = self.umls_service.get_icd10cm_from_cui(entity["cui"])  # type: ignore
                if icd_matches:
                    # Pick first match (or apply ranking/scoring logic)
                    entity["icd10cm"] = icd_matches[0]["code"]
                    entity["icd10cm_name"] = icd_matches[0]["name"]
                else:
                    entity["icd10cm"] = None
                    entity["icd10cm_name"] = None
        return normalized_entities

    def main(self) -> Dict[str, List[Entity]]:
        """
        Main method to run the service.
        """
        # Step 1: Extract entities from text
        original_entities = self.ner_concept_extraction(self.text)
        
        # Filter for disease entities and preserve all position information
        disease_entities = [
            {
                "text": entity["text"],  # type: ignore
                "label": entity["label"],  # type: ignore
                "start_char": entity["start_char"],  # type: ignore
                "end_char": entity["end_char"]  # type: ignore
            }
            for entity in original_entities 
            if entity["label"] == 'DISEASE'  # type: ignore
        ]
        deduplicated_entities = deduplicate(disease_entities)

        print("Number of Entities Extracted:", len(deduplicated_entities))
        print("Deduplicated entities with positions:", [
            f"{e['text']} ({e['start_char']}-{e['end_char']})" 
            for e in deduplicated_entities
        ])

        # Step 2: Normalize entities using UMLS
        # Convert to Entity format for normalization, preserving positions
        entities_for_normalization = [
            Entity(
                text=entity["text"],
                label=entity["label"],
                start_char=entity["start_char"],
                end_char=entity["end_char"]
            )
            for entity in deduplicated_entities
        ]
        normalized_entities = self.normalize_entities(entities_for_normalization)
        print("Normalized Entities:", normalized_entities)

        # Step 3: Match ICD codes
        entities_with_icd_codes = self.match_icd_codes(normalized_entities)
        print("Matched ICD Codes:", entities_with_icd_codes)

        return {
            "entities": original_entities,
            "normalized_entities": normalized_entities,
            "icd_codes": entities_with_icd_codes
        }

