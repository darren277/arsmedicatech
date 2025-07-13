""""""
import os
import sys

import requests

# Add the project root to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from settings import OPTIMAL_KEY, OPTIMAL_URL, logger


def test_optimal_service():
    import numpy as np

    from lib.opt.hypertension import (build_hypertension_payload,
                                      create_food_data_pd)

    food_data = create_food_data_pd()

    payload = build_hypertension_payload(food_data)

    print(payload)

    resp_without_api_key = requests.post("https://optimal.apphosting.services/optimize", json=payload, timeout=10)

    print("Response without API key:", resp_without_api_key.status_code, resp_without_api_key.text)

    assert resp_without_api_key.status_code == 403

    headers = {
        'x-api-key': OPTIMAL_KEY
    }

    resp = requests.post(
        "https://optimal.apphosting.services/optimize",
        json=payload,
        headers=headers,
        timeout=30
    )

    print(resp.status_code, resp.text)

    sol = resp.json()

    logger.debug('sol', sol)

    food_data["servings (100g)"] = np.round(sol["x"], 2)

    print(food_data)

    print(sol.keys())
    # dict_keys(['status', 'fun', 'x', 'nit'])
    # <class 'str'>
    # <class 'float'>
    # <class 'list'>
    # <class 'int'>

    for key, val in sol.items():
        print(type(val))

    print("Optimal service test passed.")


def test_optimal():
    from lib.opt.hypertension import main
    from lib.services.optimal import OptimalService

    hypertension_schema = main()

    service = OptimalService(
        url=OPTIMAL_URL,
        api_key=OPTIMAL_KEY,
        schema=hypertension_schema
    )

    res = service.send()

    print(res)



def test_patients_api(url: str = 'https://demo.arsmedicatech.com/api/patients'):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()

        # Check if the response contains the expected keys
        if isinstance(data, list) and len(data) > 0:
            first_patient = data[0]
            if 'id' in first_patient and 'last_name' in first_patient:
                print("API test passed: Received valid patient data.")
                return True
            else:
                print("API test failed: Missing expected keys in patient data.")
                return False
        else:
            print("API test failed: No patient data returned.")
            return False

    except requests.RequestException as e:
        print(f"API test failed: {e}")
        return False

if __name__ == "__main__":
    print("Running integration tests...")
    test_optimal_service()
    test_optimal()
    quit(45)
    if test_patients_api():
        print("Patients API is working correctly.")
    else:
        print("Patients API test failed.")
