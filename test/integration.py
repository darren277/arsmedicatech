""""""
import requests

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
    if test_patients_api():
        print("Patients API is working correctly.")
    else:
        print("Patients API test failed.")
