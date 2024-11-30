import pandas as pd
import matplotlib.pyplot as plt
from POWERAPI import createCSV
from EnergyCalculator import WindEnergyCalculator
from EnergyCalculator import SolarEnergyCalculator

params = {
        "parameters": "ALLSKY_SFC_SW_DWN,WS50M",
        "community": "RE",
        "longitude": -77.0369,
        "latitude": 38.9072,
        "start": "2012",
        "end": "2022",
        "format": "CSV"
    }

database = createCSV(params)

df = pd.read_csv('data.csv', skiprows=20)

ws50m_df = df[df['PARAMETER'] == 'WS50M']  # Filter rows where PARAMETER is WD50M
allsky_df = df[df['PARAMETER'] == 'ALLSKY_SFC_SW_DWN'] 

##MWh
EnergyWind = WindEnergyCalculator(ws50m_df)

##KWh
EnergySolar = SolarEnergyCalculator(allsky_df)



