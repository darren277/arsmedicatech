""""""
from lib.llm.mcp.trees import (BP_DECISION_TREE, ENHANCED_TREE, Purpose,
                               decision_tree_lookup)


def test_loan_approval():
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


def test_bp():
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
