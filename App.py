from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# This class is the backend server
# Run this in python, then go to http://127.0.0.1:5000/api/test

#tests the backend connection
@app.route('/api/test', methods=['GET'])
def test():
    return jsonify({'test_key': 'test success'}), 200

@app.route('/api/getdata', methods=['POST'])
def get_data():
    data = request.json
    lat = data.get("latitude")
    lon = data.get("longitude")

# get the latitude and longitude given a postalCode
@app.route('/api/getlatlon', methods=['POST'])
def get_latlon():
    data = request.json
    postalCode = data.get("postalcode")



# tests the HTTP POST function
# returns x^2
@app.route('/api/process', methods=['POST'])
def process_value():
    # Get data from the POST request
    data = request.json
    number = data.get("number")  # Extract "number" from JSON data

    if number is None:
        return jsonify({"error": "No number provided"}), 400

    # Perform some computation (e.g., return the square of the number)
    result = number ** 2
    return jsonify({"original": number, "result": result}), 200

if __name__ == '__main__':
    app.run(debug=True)
