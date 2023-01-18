from flask import Flask, request, jsonify
from delivery_price_calculator import calculate_delivery_fee, check_the_input, datetime_valid

app = Flask(__name__)

@app.route('/read_json', methods=['POST'])
def read_json():
    data = request.json
    if (check_the_input(data) == False):
        return "Input data is not correct, check the input"
    else:
        if datetime_valid(data["time"]) == False:
            return "Check the timestamp format"
        else:
            return calculate_delivery_fee(data)

if __name__ == "__main__":
    app.run(debug=True)