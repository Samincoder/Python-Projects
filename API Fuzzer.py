import requests

# Replace with the base URL of the API you want to fuzz
base_url = "https://api.example.com"

# Define the endpoints you want to fuzz
endpoints = [
    "/endpoint1",
    "/endpoint2",
    # Add more endpoints here
]

for endpoint in endpoints:
    url = base_url + endpoint

    response = requests.get(url)

    if response.status_code == 404:
        print(f"Received 404 response for {url}")
    else:
        try:
            json_data = response.json()
            print(f"Endpoint: {endpoint}")
            print(f"JSON Data: {json_data}\n")
        except ValueError:
            print(f"Received non-JSON response for {url}.\nResponse Content: {response.text}\n")


