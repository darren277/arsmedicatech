""""""
compare_ops = {
    '==': lambda x, y: x == y,
    '!=': lambda x, y: x != y,
    '>': lambda x, y: x > y,
    '>=': lambda x, y: x >= y,
    '<': lambda x, y: x < y,
    '<=': lambda x, y: x <= y,
}

def add_to_path(path: list, branches, subterm: str, arg):
    branch_key = next((key for key in branches if compare_ops[key[0]](arg, key[1])), None)
    if branch_key:
        path.append(f"Checked {subterm}: {arg} {branch_key[0]} {branch_key[1]}")
    return branch_key, path


def decision_tree_lookup(tree, **kwargs) -> dict:
    """
    Looks up a decision from a deterministic decision tree.

    Returns:
        A dictionary containing the final decision and the logical path taken.
    """
    path_taken = []
    current_node = tree

    # Loop until we reach a final decision (a string)
    while isinstance(current_node, dict):
        question = current_node['question']
        branches = current_node['branches']

        for i, kw in enumerate(kwargs):
            subterm = kw.replace('_', ' ')
            if subterm in question:
                branch_key, path_taken = add_to_path(path_taken, branches, subterm, kwargs[kw])
                if branch_key is None:
                    return {"decision": "Error", "reason": f"Invalid value for {subterm}: {kwargs[kw]}"}
                current_node = branches[branch_key]
                continue
        if not isinstance(current_node, dict):
            # If we reach a string, it means we've found the final decision
            break

    # At this point, current_node is the final decision string
    final_decision_parts = current_node.split(' - ')
    decision = final_decision_parts[0]
    reason = final_decision_parts[1] if len(final_decision_parts) > 1 else "No specific reason provided."

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
