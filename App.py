from flask import Flask, jsonify, request
from flask_cors import CORS
import EnergyCalculator as ec
import POWERAPI as papi

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello from Flask!"})


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
