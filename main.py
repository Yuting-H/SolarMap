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
        session['data'] = data.to_serializable_dict()
        # Use the data as needed
        return solarList
    else: return "No data found in session."

if __name__ == "__main__":
    app.run(debug=True)




