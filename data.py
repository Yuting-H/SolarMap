import pandas as pd
import matplotlib.pyplot as plt
from POWERAPI import createCSV
from EnergyCalculator import WindEnergyCalculator
from EnergyCalculator import SolarEnergyCalculator
import concurrent.futures
import threading




    
longitude = -77.0369
latitude = 38.9072
radius = 0


windEnergyList = []
sunEnergyList = []
params_list = []

def newParams(latitude,longitude):
    params = {
        "parameters": "ALLSKY_SFC_SW_DWN,WS50M",
        "community": "RE",
        "longitude": longitude,
        "latitude": latitude,
        "start": "2012",
        "end": "2022",
        "format": "CSV"
    }
    return params


lock = threading.Lock()
df_list = []

def fetch_data(params):
    data = createCSV(params)
    with lock:
        with open('data.csv', 'a') as f:
            f.write(data)
        df = pd.read_csv('data.csv', skiprows=20)
        latitude = params.get("latitude")
        longitude = params.get("longitude")
        df_list.append([df,latitude,longitude])
            
    return data


def addPoints(radius, windEnergyList, sunEnergyList):
    df_list.clear()
    params_list.clear()
    if (radius == 0):
        params_list.append(newParams(latitude,longitude))
    else: 
        params_list.append(newParams(latitude - radius,longitude + radius))
        params_list.append(newParams(latitude + radius,longitude - radius))
        params_list.append(newParams(latitude + radius,longitude + radius))
        params_list.append(newParams(latitude - radius,longitude - radius))
    radius += 1
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for param in params_list:
            futures.append(executor.submit(fetch_data, param))
    


    for df, latitude1, longitude1 in df_list:
        ws50m_df = df[df['PARAMETER'] == 'WS50M']  # Filter rows where PARAMETER is WD50M
        allsky_df = df[df['PARAMETER'] == 'ALLSKY_SFC_SW_DWN']
        windEnergyList.append([WindEnergyCalculator(ws50m_df), latitude1, longitude1])
        sunEnergyList.append([SolarEnergyCalculator(allsky_df), latitude1, longitude1])



    windEnergyList = sorted(windEnergyList, key=lambda x: x[0][12], reverse=True)
    sunEnergyList = sorted(windEnergyList, key=lambda x: x[0][12], reverse=True)
    return radius

radius = addPoints(radius, windEnergyList, sunEnergyList)
radius = addPoints(radius, windEnergyList, sunEnergyList)



"""
##MWh per 1 Standard Turbine
##$0.192 kw/h is the average cost of electricity in Canada
EnergyWind = WindEnergyCalculator(ws50m_df)
EnergySavingsWind = []
for x in EnergyWind:
    EnergySavingsWind.append(round(x * 0.192 * 1000,2))


##KWh per m^2 of solar panel
EnergySolar = SolarEnergyCalculator(allsky_df)

## Energy to Dollers based on Average
EnergySavingsSolar = []
for x in EnergySolar:
    EnergySavingsSolar.append(round(x * 0.192,2))

print(EnergySavingsSolar)
print(EnergySavingsWind)


"""
