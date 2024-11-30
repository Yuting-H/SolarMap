import pandas as pd
import matplotlib.pyplot as plt
from POWERAPI import createCSV
from EnergyCalculator import WindEnergyCalculator
from EnergyCalculator import SolarEnergyCalculator
import numpy as np

latitude = 42.9849
longitude = 81.2453

def getSolarData(longitude,latitude):
    params = {

params = {
        "parameters": "ALLSKY_SFC_SW_DWN,WS50M",
        "community": "RE",
        "longitude": longitude,
        "latitude": latitude,
        "start": "2012",
        "end": "2022",
        "format": "CSV"
    }

    df = pd.read_csv('data.csv', skiprows=20)
    createCSV(params)
    ws50m_df = df[df['PARAMETER'] == 'WS50M']
    return SolarEnergyCalculator(df)
"""
df = pd.read_csv('data.csv', skiprows=20)

ws50m_df = df[df['PARAMETER'] == 'WS50M']  # Filter rows where PARAMETER is WD50M
allsky_df = df[df['PARAMETER'] == 'ALLSKY_SFC_SW_DWN'] 

"""

##MWh
##$0.192 kw/h is the average cost of electricity in Canada

center_lat = latitude  # Example: Latitude for San Francisco
center_lon = longitude  # Example: Longitude for San Francisco
radius = 1.0  # Degrees to cover nearby points
step = 0.1  # Step size in degrees for latitude and longitude

lat_range = np.arange(center_lat - radius, center_lat + radius, step)
lon_range = np.arange(center_lon - radius, center_lon + radius, step)

# Fetch solar data for each point
results = []
for lat in lat_range:
    for lon in lon_range:
        irradiance = getSolarData(lon, lat)
        if irradiance is not None:
            results.append({"Latitude": lat, "Longitude": lon, "Irradiance": irradiance})

# Convert results to a DataFrame
df = pd.DataFrame(results)

# Rank locations by irradiance
df = df.sort_values(by="Irradiance", ascending=False)

print("Top Nearby Locations for Solar Potential:")
print(df.head())

# Visualize top nearby locations
import matplotlib.pyplot as plt

plt.scatter(df['Longitude'], df['Latitude'], c=df['Irradiance'], cmap='hot', s=50)
plt.colorbar(label='Irradiance (kWh/m²/day)')
plt.title('Nearby Solar Potential')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()




EnergyWind = WindEnergyCalculator(ws50m_df)
EnergySavingsWind = []
for x in EnergyWind:
    EnergySavingsWind.append(round(x * 0.192 * 1000,2))


##KWh
EnergySolar = SolarEnergyCalculator(allsky_df)

## Energy to Dollers based on Average
EnergySavingsSolar = []
for x in EnergySolar:
    EnergySavingsSolar.append(round(x * 0.192,2))

print(EnergySavingsSolar)
print(EnergySavingsWind)



