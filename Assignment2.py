# Import necessary libraries
import requests
import json
import pytest

# Define global variables for the API base URL and authentication token
BASE_URL = "https://gorest.co.in"
AUTH_TOKEN = "419420c65304b856b9870a60a2c278337f8a4b64ef78ddc7c78351bf68dc9519"
headers = {"Authorization": f"Bearer {AUTH_TOKEN}"}


# Function to authenticate a user
def authenticate_user():
    data = {
        "name": "Kanishka",
        "email": "niwggwa@example",
        "gender": "female",
        "status": "active"
    }

    auth_endpoint = f"{BASE_URL}/public/v2/users"

    # Make a POST request to authenticate the user
    response = requests.post(auth_endpoint, data=data, headers=headers)

    # Check if authentication was successful
    if response.status_code == 201:
        print("Authentication successful.")
    else:
        print("Authentication failed.")

    return response


# Function to retrieve and validate user profile information
def get_user_profile(user_id):
    profile_endpoint = f"{BASE_URL}/public/v2/users/{user_id}"

    # Make a GET request to retrieve user profile
    response = requests.get(profile_endpoint, headers=headers)

    # Validate the response and print relevant information
    if response.status_code == 200:

        user_profile = response.json()
        print("\nUser Profile : ", user_profile)
    else:
        print("Failed to retrieve user profile.")

    return response


# Function to update user profile information
def update_user_profile(user_id, new_display_name):
    update_endpoint = f"{BASE_URL}/public/v2/users/{user_id}"
    update_payload = {"name": new_display_name}

    # Make a PUT request to update user profile
    response = requests.put(update_endpoint, headers=headers, data=update_payload)

    # Check if the profile was updated successfully
    if response.status_code == 200:
        print("\nUser profile updated successfully.")
    else:
        print("\nFailed to update user profile.")

    return response


def delete_user_profile(user_id):
    delete_endpoint = f"{BASE_URL}/public/v2/users/{user_id}"

    # Make a delete request to delete user profile
    response = requests.delete(delete_endpoint, headers=headers)

    # Validate the response and print relevant information
    if response.status_code == 204:
        print("\nUser Profile deleted successfully")
    else:
        print("\nFailed to delete user profile.")

    return response


# PyTest fixture to authenticate user before tests
@pytest.fixture(scope="module")
def authenticated_user():
    response = authenticate_user()
    assert response.status_code == 201, "Authentication failed."
    return json.loads(response.text)["id"]


# PyTest test cases
def test_get_user_profile(authenticated_user):
    response = get_user_profile(authenticated_user)
    assert response.status_code == 200, "Failed to retrieve user profile."


def test_update_user_profile(authenticated_user):
    response = update_user_profile(authenticated_user, "New Display Name")
    assert response.status_code == 200, "Failed to update user profile."
    print("User profile after update : ", response.json())


def test_delete_user_profile(authenticated_user):
    response = delete_user_profile(authenticated_user)
    assert response.status_code == 204, "Failed to delete user profile."
