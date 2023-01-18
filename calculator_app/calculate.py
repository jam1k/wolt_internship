from flask import Flask, request, jsonify
from delivery_price_calculator import calculate_delivery_fee, check_the_input

app = Flask(__name__)

@app.route('/read_json', methods=['POST'])
def read_json():
    data = request.json
    errors = check_the_input(data)
    if bool(errors):
        return jsonify(errors), 400
    else:
        response = calculate_delivery_fee(data)
        return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)