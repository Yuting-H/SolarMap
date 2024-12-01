from flask import Flask, request, jsonify, redirect, url_for, session
from Data import Data;

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/initialize', methods = ['GET', 'POST'])
def initialize():
    if request.method == 'POST':
        lat = float(request.form['lat'])
        lon = float(request.form['lon'])
        data = Data(lat,lon)
        session['data'] = data.to_serializable_dict()
        return jsonify(lat), 201

    return '''
        <form method="post">
            Initial Latitude: <input type="text" name="lat"><br>
            Initial Longitude: <input type="text" name="lon"><br>
            <input type="submit" value="Initialize">
        </form>
        '''

@app.route("/")
def home():
    return "Home"

@app.route("/getSolar", methods = ["GET"])
def getSolar():
    if 'data' in session:
        data_dict = session['data']
        data = Data.from_serializable_dict(Data, data_dict)
        solarList = data.getSolarEnergyList();
        solarDic = {}
        for i in range(len(solarList)):
            solarDic[str(i)] = {"jan": solarList[i][0][0], "feb": solarList[i][0][1], "mar": solarList[i][0][2], "apr": solarList[i][0][3], "may": solarList[i][0][4], "jun": solarList[i][0][5], "jul": solarList[i][0][6], 
                                "aug": solarList[i][0][7], "sep": solarList[i][0][8], "oct": solarList[i][0][9], "nov": solarList[i][0][10], "dec": solarList[i][0][11], "ann": solarList[i][0][12], "latitude": solarList[i][1], "longitude": solarList[i][2]
                    }
        session['data'] = data.to_serializable_dict()
        # Use the data as needed
        return jsonify(solarDic)
    else: return "No data found in session."
@app.route("/getSortedSolar", methods = ["GET"])
def getSortedSolar():
    if 'data' in session:
        data_dict = session['data']
        data = Data.from_serializable_dict(Data, data_dict)
        solarList = data.getSolarEnergyList();
        solarSortedDic = {}
        for i in range(len(solarList)):
            solarSortedDic[str(i)] = {"jan": solarList[i][0][0], "feb": solarList[i][0][1], "mar": solarList[i][0][2], "apr": solarList[i][0][3], "may": solarList[i][0][4], "jun": solarList[i][0][5], "jul": solarList[i][0][6], 
                                "aug": solarList[i][0][7], "sep": solarList[i][0][8], "oct": solarList[i][0][9], "nov": solarList[i][0][10], "dec": solarList[i][0][11], "ann": solarList[i][0][12], "latitude": solarList[i][1], "longitude": solarList[i][2]
                    }
        session['data'] = data.to_serializable_dict()
        # Use the data as needed
        return jsonify(solarSortedDic)
    else: return "No data found in session."

@app.route("/getWind", methods = ["GET"])
def getWind():
    if 'data' in session:
        data_dict = session['data']
        data = Data.from_serializable_dict(Data, data_dict)
        windList = data.getWindEnergyList();
        windDic = {}
        for i in range(len(windList)):
            windDic[str(i)] = {"jan": windList[i][0][0], "feb": windList[i][0][1], "mar": windList[i][0][2], "apr": windList[i][0][3], "may": windList[i][0][4], "jun": windList[i][0][5], "jul": windList[i][0][6], 
                                "aug": windList[i][0][7], "sep": windList[i][0][8], "oct": windList[i][0][9], "nov": windList[i][0][10], "dec": windList[i][0][11], "ann": windList[i][0][12], "latitude": windList[i][1], "longitude": windList[i][2]
                    }
        session['data'] = data.to_serializable_dict()
        # Use the data as needed
        return jsonify(windDic)
    else: return "No data found in session."

@app.route("/getSortedWind", methods = ["GET"])
def getSortedWind():
    if 'data' in session:
        data_dict = session['data']
        data = Data.from_serializable_dict(Data, data_dict)
        windList = data.getWindEnergyList();
        windSortedDic = {}
        for i in range(len(windList)):
            windSortedDic[str(i)] = {"jan": windList[i][0][0], "feb": windList[i][0][1], "mar": windList[i][0][2], "apr": windList[i][0][3], "may": windList[i][0][4], "jun": windList[i][0][5], "jul": windList[i][0][6], 
                                "aug": windList[i][0][7], "sep": windList[i][0][8], "oct": windList[i][0][9], "nov": windList[i][0][10], "dec": windList[i][0][11], "ann": windList[i][0][12], "latitude": windList[i][1], "longitude": windList[i][2]
                    }
        session['data'] = data.to_serializable_dict()
        # Use the data as needed
        return jsonify(windSortedDic)
    else: return "No data found in session."


@app.route("/addPointsCircle", methods = ["POST"])
def addPointsCircle():
    if 'data' in session:
        data_dict = session['data']
        data = Data.from_serializable_dict(Data, data_dict)
        data.addPoints()
        session['data'] = data.to_serializable_dict()
        return "Added Circles"
    else: return "No data found in session."



if __name__ == "__main__":
    app.run(debug=True)




