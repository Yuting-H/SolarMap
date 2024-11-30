import requests

# Define the API endpoint and parameters
url = "https://power.larc.nasa.gov/api/temporal/daily/point"
params = {
    "parameters": "ALLSKY_SFC_SW_DNI,WD50M",
    "community": "ag",
    "longitude": -77.0369,
    "latitude": 38.9072,
    "start": "20240101",
    "end": "20240131",
    "format": "CSV"
}

# Send the GET request
response = requests.get(url, params=params)


# Check for a successful response
if response.status_code == 200:
    # Write the response content to a CSV file
    with open('data.csv', 'w') as file:
        file.write(response.text)
    print("CSV file saved as 'data.csv'")
else:
    print(f"Error: {response.status_code}")