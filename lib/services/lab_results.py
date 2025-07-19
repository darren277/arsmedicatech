"""
Lab Results Service

Until we have any APIs to connect to, this will use some placeholder data.
"""

from typing import Any, Dict

BIL_PER_LITER = "10*9/L"
TRIL_PER_LITER = "10*12/L"
G_PER_LITER = "g/L"
LITER_PER_LITER = "L/L"
FL = "fl"
PG = "pg"
PERCENT = "%"

MMOL_PER_LITER = "mmol/L"
UMOL_PER_LITER = "umol/L"
NULL = None

U_PER_LITER = "U/L"

INF = 9999


LabResult = Dict[str, Any]
LabResults = Dict[str, LabResult]

hematology: LabResults = {
	"WBC": {"result": 8.9, "reference_range": [4.0, 10.0], "units": BIL_PER_LITER, "description": "White Blood Cell Count"},
	"RBC": {"result": 4.91, "reference_range": [4.20, 5.40], "units": TRIL_PER_LITER, "description": "Red Blood Cell Count"},
	"Hemoglobin": {"result": 144, "reference_range": [135, 170], "units": G_PER_LITER, "description": "Hemoglobin"},
	"Hematocrit": {"result": 0.44, "reference_range": [0.40, 0.50], "units": LITER_PER_LITER, "description": "Hematocrit"},
	"MCV": {"result": 89, "reference_range": [82, 98], "units": FL, "description": "Mean Corpuscular Volume"},
	"MCH": {"result": 29.3, "reference_range": [27.5, 33.5], "units": PG, "description": "Mean Corpuscular Hemoglobin"},
	"MCHC": {"result": 329, "reference_range": [300, 370], "units": G_PER_LITER, "description": "Mean Corpuscular Hemoglobin Concentration"},
	"RDW": {"result": 12.5, "reference_range": [11.5, 14.5], "units": PERCENT, "description": "Red Cell Distribution Width"},
	"Platelet Count": {"result": 274, "reference_range": [150, 400], "units": BIL_PER_LITER, "description": "Platelet Count"},
}

differential_hematology: LabResults = {
	"Neutrophils": {"result": 5.4, "reference_range": [2.0, 7.5], "units": BIL_PER_LITER, "description": "Neutrophils"},
	"Lymphocytes": {"result": 2.3, "reference_range": [1.0, 4.0], "units": BIL_PER_LITER, "description": "Lymphocytes"},
	"Monocytes": {"result": 1.0, "reference_range": [0.1, 0.8], "units": BIL_PER_LITER, "description": "Monocytes"},
	"Eosinophils": {"result": 0.2, "reference_range": [0.0, 0.7], "units": BIL_PER_LITER, "description": "Eosinophils"},
	"Basophils": {"result": 0.1, "reference_range": [0.0, 0.2], "units": BIL_PER_LITER, "description": "Basophils"},
	"Granulocytes Immature": {"result": 0.0, "reference_range": [0.0, 0.1], "units": BIL_PER_LITER, "description": "Granulocytes Immature"},
}

general_chemistry: LabResults = {
	"Sodium": {"result": 138, "reference_range": [135, 145], "units": MMOL_PER_LITER, "description": "Sodium"},
	"Creatinine": {"result": 81, "reference_range": [45, 110], "units": UMOL_PER_LITER, "description": "Creatinine"},
	"Estimated GFR": {"result": 104, "reference_range": [60, INF], "units": NULL, "notes": "Fill this in later.", "description": "Estimated Glomerular Filtration Rate"},
	"Albumin": {"result": 51, "reference_range": [35, 50], "units": G_PER_LITER, "description": "Albumin"},
	"Total Bilirubin": {"result": 7, "reference_range": [0, 17], "units": UMOL_PER_LITER, "description": "Total Bilirubin"},
	"Conjugated Bilirubin": {"result": 2, "reference_range": [0, 8], "units": UMOL_PER_LITER, "description": "Conjugated Bilirubin"},
	"Alkaline Phosphatase": {"result": 93, "reference_range": [40, 145], "units": U_PER_LITER, "description": "Alkaline Phosphatase"},
	"Gamma GT": {"result": 79, "reference_range": [0, 65], "units": U_PER_LITER, "description": "Gamma GT"},
	"Alanine Aminotransferase": {"result": 33, "reference_range": [0, 50], "units": U_PER_LITER, "description": "Alanine Aminotransferase"},
	"Aspartate Aminotransferase": {"result": 37, "reference_range": [0, 36], "units": U_PER_LITER, "description": "Aspartate Aminotransferase"},
	"Lactate Dehydrogenase": {"result": 212, "reference_range": [0, 225], "units": U_PER_LITER, "description": "Lactate Dehydrogenase"},
}

serum_proteins: LabResults = {
	"IgG": {"result": 13.85, "reference_range": [7.0, 16.0], "units": G_PER_LITER, "description": "IgG"},
	"IgA": {"result": 1.15, "reference_range": [0.7, 4.0], "units": G_PER_LITER, "description": "IgA"},
	"IgM": {"result": 0.63, "reference_range": [0.4, 2.3], "units": G_PER_LITER, "description": "IgM"},
	"Ceruloplasmin": {"result": 0.32, "reference_range": [0.19, 0.31], "units": G_PER_LITER, "description": "Ceruloplasmin"},
	"Alpha 1 Antitrypsin": {"result": 1.28, "reference_range": [0.9, 2.18], "units": G_PER_LITER, "description": "Alpha 1 Antitrypsin"},
}


class LabResultsService:
    """
    Service for getting lab results.

    Until we have any APIs to connect to, this will use some placeholder data.
    """
    
    def __init__(self, **lab_results: LabResults) -> None:
        """
        Initialize the lab results service with the given lab results.

        Args:
            lab_results: A dictionary of lab results.
        """
        self.lab_results = lab_results
