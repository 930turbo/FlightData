import requests
import pandas as pd
import matplotlib.pyplot as plt

# API endpoint for flight data
url = 'https://opensky-network.org/api/states/all'

# Function to get flight data for a specific plane
def get_flight_data(call_sign):
    # Make a request to the OpenSky API
    response = requests.get(url)
    data = response.json()
    # Create a pandas dataframe from the API data
    flight_data = pd.DataFrame(data['states'], columns=data['columns'])
    # Filter flight data for the specified call sign
    flight_data = flight_data[flight_data['callsign'] == call_sign]
    return flight_data

# Get user input
call_sign = input("Enter a plane's call sign: ")
# Get flight data for the specified call sign
flight_data = get_flight_data(call_sign)

# Visualize the flight data
plt.scatter(flight_data['longitude'], flight_data['latitude'])
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Flight Data for ' + call_sign)
plt.show()
