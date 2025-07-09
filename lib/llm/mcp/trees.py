""""""
import re
from typing import Any, Callable, Dict, Tuple, Union, Iterable, Annotated
import enum

from pydantic import Field

compare_ops: dict[str, Callable[[Any, Any], bool]] = {}

def register_compare_op(symbol: str, func: Callable[[Any, Any], bool]) -> None:
    """Allow the tree author to plug‑in new binary operators at runtime."""
    compare_ops[symbol] = func

register_compare_op('==', lambda x, y: x == y)
register_compare_op('!=', lambda x, y: x != y)
register_compare_op('>',  lambda x, y: x >  y)
register_compare_op('>=', lambda x, y: x >= y)
register_compare_op('<',  lambda x, y: x <  y)
register_compare_op('<=', lambda x, y: x <= y)
register_compare_op('in',     lambda x, y: x in y)
register_compare_op('not in', lambda x, y: x not in y)
register_compare_op('regex',  lambda x, pattern: re.fullmatch(pattern, str(x)) is not None)

BranchKey = Union[Tuple[str, Any], Callable[[Any], bool], Any]


def _choose_branch(
        branches: Dict[BranchKey, Any],
       arg: Any,
       subterm: str,
       path: list[str]
    ) -> Tuple[Any | None, list[str]]:

    for key, target in branches.items():
        # a)  Callable predicate
        if callable(key):
            if key(arg):
                path.append(f"Checked {subterm}: predicate {key.__name__} → True")
                return key, path
        # b)  (‘<op>’, reference)
        elif isinstance(key, tuple) and len(key) == 2:
            op, ref = key
            if op not in compare_ops:
                raise ValueError(f"Unsupported operator {op!r}. Register it first.")
            if compare_ops[op](arg, ref):
                path.append(f"Checked {subterm}: {arg!r} {op} {ref!r}")
                return key, path
        # c)  Literal / Enum → equality
        else:
            if arg == key:
                path.append(f"Checked {subterm}: {arg!r} == {key!r}")
                return key, path
    # no match
    return None, path


def decision_tree_lookup(tree: Dict[str, Any], **kwargs) -> Dict[str, Any]:
    """
    Looks up a decision from a deterministic decision tree.

    Returns:
        A dictionary containing the final decision and the logical path taken.
    """
    path_taken: list[str] = []
    current_node = tree

    # Loop until we reach a final decision (a string)
    while isinstance(current_node, dict):
        question: str = current_node['question']
        branches: Dict[BranchKey, Any] = current_node['branches']
        matched = False

        for kw_name, value in kwargs.items():
            subterm = kw_name.replace('_', ' ') # crude NLP: map loan_purpose → "loan purpose"
            if subterm in question:
                key, path_taken = _choose_branch(branches, value, subterm, path_taken)
                if key is None:
                    return {"decision": "Error",
                            "reason": f"Invalid value for {subterm}: {value!r}",
                            "path_taken": path_taken}
                current_node = branches[key]
                matched = True
                break

        if not matched:
            return {"decision": "Error",
                    "reason": f"Question {question!r} could not be answered with supplied arguments.",
                    "path_taken": path_taken}

    # At this point, current_node is the final decision string: We've hit a leaf (a string)
    decision, *rest = str(current_node).split(' - ', 1)
    reason = rest[0] if rest else "No specific reason provided."
    return {
        "decision": decision,
        "reason": reason,
        "path_taken": path_taken
    }



## EXAMPLE WITH INTEGER COMPARISONS ##

LOAN_DECISION_TREE = {
    'question': 'What is your credit score?',
    'branches': {
        ('<', 640): 'Declined - Credit score too low',
        ('>=', 640): {
            'question': 'What is your annual income?',
            'branches': {
                ('<', 50000): {
                    'question': 'What is the requested loan amount?',
                    'branches': {
                        ('<=', 10000): 'Approved - Small loan with moderate income',
                        ('>', 10000): 'Declined - Loan amount too high for income'
                    }
                },
                ('>=', 50000): 'Approved - Strong income and credit score'
            }
        }
    }
}

def loan_decision_tree_lookup(credit_score: int, income: int, requested_amount: int) -> dict:
    """
    Looks up a loan decision from a deterministic decision tree.

    Args:
        credit_score: The applicant's credit score.
        income: The applicant's annual income.
        requested_amount: The amount of the loan being requested.

    Returns:
        A dictionary containing the final decision and the logical path taken.
    """
    return decision_tree_lookup(
        LOAN_DECISION_TREE,
        credit_score=credit_score,
        income=income,
        requested_amount=requested_amount
    )

tool_definition = {
    "type": "function",
    "function": {
        "name": "decision_tree_lookup",
        "description": "Determines loan eligibility and outcome by checking against a set of financial rules.",
        "parameters": {
            "type": "object",
            "properties": {
                "credit_score": {
                    "type": "integer",
                    "description": "The applicant's credit score, e.g., 720"
                },
                "income": {
                    "type": "integer",
                    "description": "The applicant's total annual income, e.g., 65000"
                },
                "requested_amount": {
                    "type": "integer",
                    "description": "The total amount of the loan requested by the applicant"
                }
            },
            "required": ["credit_score", "income", "requested_amount"]
        }
    }
}


# ────────────────────────────────────────────────────────────
# Example: using Enum + membership tests
# ────────────────────────────────────────────────────────────
class Purpose(enum.Enum):
    HOME       = "home"
    CAR        = "car"
    EDUCATION  = "education"

ENHANCED_TREE = {
    "question": "What is the loan purpose?",
    "branches": {
        Purpose.HOME: "Declined - Mortgages not offered",
        Purpose.CAR: {
            "question": "What is your credit score?",
            "branches": {
                ('<', 600):  "Declined - Credit too low for auto loan",
                ('>=', 600): "Approved - Auto loan"
            }
        },
        Purpose.EDUCATION: {
            "question": "Which country is your university located in?",
            # sets must be hashable → use frozenset
            "branches": {
                ('in',     frozenset({'US', 'Canada'})): "Approved - Domestic study",
                ('not in', frozenset({'US', 'Canada'})): "Declined - Foreign study"
            }
        }
    }
}

def enhanced_tree_lookup(purpose: Purpose, credit_score: int, country: str) -> dict:
    """
    Looks up a loan decision from an enhanced decision tree using Enum and membership tests.

    Args:
        purpose: The purpose of the loan (Purpose Enum).
        credit_score: The applicant's credit score.
        country: The country where the university is located.

    Returns:
        A dictionary containing the final decision and the logical path taken.
    """
    return decision_tree_lookup(
        ENHANCED_TREE,
        purpose=purpose,
        credit_score=credit_score,
        country=country
    )

tool_definition_enhanced = {
    "type": "function",
    "function": {
        "name": "enhanced_tree_lookup",
        "description": "Determines loan eligibility and outcome by checking against a set of financial rules with enhanced features.",
        "parameters": {
            "type": "object",
            "properties": {
                "purpose": {
                    "type": "string",
                    "enum": [e.value for e in Purpose],
                    "description": "The purpose of the loan, e.g., 'home', 'car', 'education'"
                },
                "credit_score": {
                    "type": "integer",
                    "description": "The applicant's credit score, e.g., 720"
                },
                "country": {
                    "type": "string",
                    "description": "The country where the university is located, e.g., 'US', 'Canada'"
                }
            },
            "required": ["purpose", "credit_score", "country"]
        }
    }
}

result = decision_tree_lookup(
    ENHANCED_TREE,
    loan_purpose=Purpose.EDUCATION,
    country='US',
    credit_score=720
)
print(result)

assert result['decision'] == "Approved"
assert result['reason'] == "Domestic study"
assert "<Purpose.EDUCATION: 'education'> == <Purpose.EDUCATION: 'education'>" in result['path_taken'][0]
assert "'US' in frozenset" in result['path_taken'][1]



# ---------------
# Medical example
# ---------------

# ───────────────────────────────────────────────────────────
#  Proof‑of‑concept decision tree: Blood‑pressure categories
#  (adapted from ACC/AHA 2017 guideline levels)
# ───────────────────────────────────────────────────────────
BP_DECISION_TREE = {
    "question": "What is your diastolic blood pressure?",
    "branches": {
        # Hypertensive crisis if DBP ≥120 mm Hg regardless of SBP
        ('>=', 120): "Hypertensive crisis - Seek emergency care immediately",
        # Otherwise we still need SBP to finish the classification
        ('<', 120): {
            "question": "What is your systolic blood pressure?",
            "branches": {
                # Crisis if SBP ≥180 mm Hg (even though DBP <120)
                ('>=', 180): "Hypertensive crisis - Seek emergency care immediately",

                # Hypertension Stage 2
                ('>=', 140): "Hypertension Stage 2 - Discuss medication and lifestyle changes with a clinician",

                # Hypertension Stage 1
                ('in', range(130, 140)): "Hypertension Stage 1 - Lifestyle changes and possible medication (clinician‑guided)",

                # Elevated BP (SBP 120‑129 *and* DBP < 80, which we already know here)
                ('in', range(120, 130)): "Elevated blood pressure - Adopt heart‑healthy lifestyle",

                # Normal BP (SBP < 120 and DBP < 80)
                ('<', 120): "Normal blood pressure - Maintain current healthy habits"
            }
        }
    }
}

def blood_pressure_decision_tree_lookup(
        systolic_blood_pressure: Annotated[
            int, Field(description="The patient's systolic blood pressure, e.g., 128")
        ],
        diastolic_blood_pressure: Annotated[
            int, Field(description="The patient's diastolic blood pressure, e.g., 78")
        ],
) -> dict:
    """
    Looks up a blood pressure classification from a decision tree.

    Args:
        systolic_blood_pressure: The patient's systolic blood pressure.
        diastolic_blood_pressure: The patient's diastolic blood pressure.

    Returns:
        A dictionary containing the final classification and the logical path taken.
    """
    return decision_tree_lookup(
        BP_DECISION_TREE,
        systolic_blood_pressure=systolic_blood_pressure,
        diastolic_blood_pressure=diastolic_blood_pressure
    )

tool_definition_bp = {
    "type": "function",
    "function": {
        "name": "blood_pressure_decision_tree_lookup",
        "description": "Classifies blood pressure levels and provides recommendations based on systolic and diastolic values.",
        "parameters": {
            "type": "object",
            "properties": {
                "systolic_blood_pressure": {
                    "type": "integer",
                    "description": "The patient's systolic blood pressure, e.g., 128"
                },
                "diastolic_blood_pressure": {
                    "type": "integer",
                    "description": "The patient's diastolic blood pressure, e.g., 78"
                }
            },
            "required": ["systolic_blood_pressure", "diastolic_blood_pressure"]
        }
    }
}

result = decision_tree_lookup(
    BP_DECISION_TREE,
    systolic_blood_pressure=128,
    diastolic_blood_pressure=78
)
print(result)

assert result['decision'] == "Elevated blood pressure"
assert result['reason'] == "Adopt heart‑healthy lifestyle"
assert "Checked diastolic blood pressure: 78 < 120" in result['path_taken'][0]
assert "Checked systolic blood pressure: 128 in range(120, 130)" in result['path_taken'][1]
