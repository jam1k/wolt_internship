from flask import Flask, request, jsonify
from delivery_price_calculator import calculate_delivery_fee

app = Flask(__name__)

@app.route('/read_json', methods=['POST'])
def read_json():
    data = request.json
    return calculate_delivery_fee(data)

if __name__ == "__main__":
    app.run(debug=True)