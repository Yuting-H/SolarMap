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
        listSolar = session['sunEnergyList']
        # Use the data as needed
        return f"{len(listSolar)}"
    else: return "No data found in session."

if __name__ == "__main__":
    app.run(debug=True)




