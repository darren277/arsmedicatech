""""""
import pandas as pd

from lib.services.optimal import OptimalSchema, OptimalMetadata


def create_food_data_pd():
    food_data = pd.DataFrame({
        "food": ["Oats", "Salmon", "Spinach", "Banana", "Almonds", "Chicken Breast", "White Bread", "Cheese"],
        "sodium_mg": [2, 59, 79, 1, 1, 70, 490, 621],
        "potassium_mg": [429, 628, 558, 358, 705, 256, 115, 98],
        "fiber_g": [10.6, 0, 2.2, 2.6, 12.5, 0, 2.7, 0],
        "saturated_fat_g": [1.1, 1.0, 0, 0.1, 3.8, 1.0, 0.8, 18.9],
        "calories": [389, 208, 23, 89, 579, 165, 265, 402],
        "allergy": [0, 0, 0, 0, 1, 0, 0, 0] # Allergy flag (Boolean)
    })

    # Convert to numpy arrays
    sodium = food_data["sodium_mg"].values
    potassium = food_data["potassium_mg"].values
    fiber = food_data["fiber_g"].values
    sat_fat = food_data["saturated_fat_g"].values
    calories = food_data["calories"].values
    allergy = food_data["allergy"].values

    # Number of food items
    n = len(food_data)

    return food_data


def build_hypertension_payload(df: pd.DataFrame) -> dict:
    payload = {
        "meta": {"problem_id": "htn-diet-v1", "solver": "scipy_slsqp", "sense": "minimize"},
        "variables": [{"name": f"x{i}", "lower": 0, "upper": 10} for i in range(len(df))],
        "parameters": {col: df[col].astype(float).tolist()
                       for col in ["sodium_mg", "potassium_mg",
                                    "fiber_g", "saturated_fat_g",
                                    "calories", "allergy"]},
        "objective": {
            "expr": ("0.6*dot(sodium_mg,x) + 0.3*dot(saturated_fat_g,x)"
                     " - 0.4*dot(potassium_mg,x) - 0.2*dot(fiber_g,x)")
        },
        "constraints": [
            {"type": "ineq", "expr": "2000 - dot(calories,x)"},
            {"type": "ineq", "expr": "sum(x) - 5"},
            {"type": "eq",   "expr": "dot(allergy,x)"}
        ],
        "initial_guess": [1.0]*len(df)
    }
    return payload



def main():
    df = create_food_data_pd()
    hypertension_schema = OptimalSchema(
        meta=OptimalMetadata(problem_id="htn-diet-v1", solver="scipy_slsqp", sense="minimize"),
        variables=[{"name": f"x{i}", "lower": 0, "upper": 10} for i in range(len(df))],
        parameters={col: df[col].astype(float).tolist()
                       for col in ["sodium_mg", "potassium_mg",
                                    "fiber_g", "saturated_fat_g",
                                    "calories", "allergy"]},
        objective={"expr": "0.6*dot(sodium_mg,x) + 0.3*dot(saturated_fat_g,x) - "
                           "0.4*dot(potassium_mg,x) - 0.2*dot(fiber_g,x)"},
        constraints=[
            {"type": "ineq", "expr": "2000 - dot(calories,x)"},
            {"type": "ineq", "expr": "sum(x) - 5"},
            {"type": "eq",   "expr": "dot(allergy,x)"}
        ],
        initial_guess=[1.0]*len(df)
    )

    return hypertension_schema
