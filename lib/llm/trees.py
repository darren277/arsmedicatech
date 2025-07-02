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


