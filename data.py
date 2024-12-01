import pandas as pd
from POWERAPI import createCSV
from EnergyCalculator import EnergyCalculator
import concurrent.futures
import threading


## Data class 
class Data:
    latitude = 0
    longitude = 0
    radius = 0
    windEnergyList = []
    sunEnergyList = []
    params_list = []
    lock = threading.Lock()
    df_list = []
    energyCalc = EnergyCalculator()

    ## Initalizes, Creates First Node
    def __init__(self, latitude, longitude) -> None:
        self.latitude = latitude
        self.longitude = longitude
        self.radius = 0
        self.windEnergyList = []
        self.sunEnergyList = []
        self.params_list = []
        self.lock = threading.Lock()
        self.df_list = []
        self.energyCalc = EnergyCalculator()
        self.addPoints()


    def to_serializable_dict(self):
        return {
            'latitude': self.latitude,
            'longitude': self.longitude,
            'radius': self.radius,
            'windEnergyList': self.windEnergyList,
            'sunEnergyList': self.sunEnergyList,
            'params_list': self.params_list,
            'df_list': [
            {
                'df': df.to_dict(orient='records'),
                'latitude': lat,
                'longitude': lon
            }
            for df, lat, lon in self.df_list
        ]
            # Exclude self.lock and self.energyCalc
        }
    
    
    def from_serializable_dict(cls, data):
        obj = cls(data['latitude'], data['longitude'])
        obj.radius = data['radius']
        obj.windEnergyList = data['windEnergyList']
        obj.sunEnergyList = data['sunEnergyList']
        obj.params_list = data['params_list']
        df_list_serialized = data.get('df_list', [])
        obj.df_list = [[pd.DataFrame.from_records(item['df']),item['latitude'],item['longitude']] for item in df_list_serialized ]
        # Reinitialize lock and energyCalc
        obj.lock = threading.Lock()
        obj.energyCalc = EnergyCalculator()
        return obj

    def newParams(self,latitude,longitude):
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


    

    def fetch_data(self, params):
        data = createCSV(params)
        with self.lock:
            with open('data.csv', 'a') as f:
                f.write(data)
            df = pd.read_csv('data.csv', skiprows=20)
            latitude = params.get("latitude")
            longitude = params.get("longitude")
            self.df_list.append([df,latitude,longitude])
                
        return data

    ## Expands the circle
    def addPoints(self):
    
        self.df_list.clear()
        self.params_list.clear()
        if (self.radius == 0):
            self.params_list.append(self.newParams(self.latitude,self.longitude))
        else: 
            self.params_list.append(self.newParams(self.latitude - self.radius,self.longitude + self.radius))
            self.params_list.append(self.newParams(self.latitude + self.radius,self.longitude - self.radius))
            self.params_list.append(self.newParams(self.latitude + self.radius,self.longitude + self.radius))
            self.params_list.append(self.newParams(self.latitude - self.radius,self.longitude - self.radius))
        self.radius += 1
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for param in self.params_list:
                futures.append(executor.submit(self.fetch_data, param))
        


        for df, latitude1, longitude1 in self.df_list:
            ws50m_df = df[df['PARAMETER'] == 'WS50M']  # Filter rows where PARAMETER is WD50M
            allsky_df = df[df['PARAMETER'] == 'ALLSKY_SFC_SW_DWN']
            self.windEnergyList.append([self.energyCalc.WindEnergyCalculator(ws50m_df), latitude1, longitude1])
            self.sunEnergyList.append([self.energyCalc.SolarEnergyCalculator(allsky_df), latitude1, longitude1])

        
    ## Returns unsorted Wind Energy list
    def getWindEnergyList(self):
        return self.windEnergyList
    
    ## Returns unsorted Solar Energy List
    def getSolarEnergyList(self):
        return self.sunEnergyList
    
    ## Returns Sorted Wind Energy List
    def getSortedWindEnergyList(self):
        windEnergyList = self.windEnergyList.copy()
        windEnergyList = sorted(windEnergyList, key=lambda x: x[0][12], reverse=True)
        return windEnergyList
    

    ## Returns Sorted Solar Energy List
    def getSortedSolarEnergyList(self):
        solarEnergyList = self.sunEnergyList.copy()
        solarEnergyList = sorted(solarEnergyList, key=lambda x: x[0][12], reverse=True)
        return solarEnergyList
    
    ## Returns Orginal Point Wind Energy
    def getOriginalPointWindEnergy(self):
        return self.windEnergyList[0][0]
    
    ## Returns Original
    def getOriginalPointSolarEnergy(self):
        return self.sunEnergyList[0][0]

    ## Sets Radius
    def setRadius(self, radius):
        self.radius = radius

    ## Sets Longitude
    def setLongitude(self, longitude):
        self.longitude = longitude

    ## Sets Latitude
    def setLatitude(self, latitude):
        self.longitude = latitude

    
    
        
    
    


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
