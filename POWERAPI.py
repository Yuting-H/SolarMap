import requests

def createCSV(params):

    #API and Parameters
    url = "https://power.larc.nasa.gov/api/temporal/monthly/point"

        
    # Send the GET request
    response = requests.get(url, params=params)

    # Check for a successful response
    if response.status_code == 200:
        # Write the response content to a CSV file
        with open('data.csv', 'w') as file:
            return response.text
        print("CSV file saved as 'data.csv'")
    else:
        print(f"Error: {response.status_code}")