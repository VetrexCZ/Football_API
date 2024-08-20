from dotenv import load_dotenv
import requests
import pytest
import os

url = "https://v3.football.api-sports.io/"

load_dotenv()
headers = {
    'x-rapidapi-key': os.getenv("API_KEY"),
    'x-rapidapi-host': 'v3.football.api-sports.io'
}


def test_status_code():
    """Test to ensure the API is reachable and returns a status code of 200."""
    response = requests.get(url, headers=headers)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"


def test_content_type():
    """Test to ensure the API returns JSON data."""
    response = requests.get(url + "/teams", headers=headers)
    assert response.headers["Content-Type"] == "application/json", \
        f"Expected Content-Type application/json, but got {response.headers['Content-Type']}"


@pytest.mark.parametrize("country", [
    "england",
    "spain",
    "italy",
    "germany",
    "france"
])
def test_teams_endpoint(country):
    """Parameterized test to check the '/teams' endpoint for various countries."""
    params = {"country": country}

    response = requests.get(url + "/teams", headers=headers, params=params)

    data = response.json()

    assert "response" in data, "Response does not contain 'response' key"

    assert len(data["response"]) > 0, f"Response is empty for country: {country}"

    first_team = data["response"][0]
    assert "team" in first_team, "First team does not contain 'team' key"


if __name__ == "__main__":
    pytest.main()
