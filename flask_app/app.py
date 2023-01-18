from flask import Flask, request, jsonify, make_response
from delivery_price_calculator import calculate_delivery_fee, check_the_input, datetime_valid

app = Flask(__name__)

@app.route('/read_json', methods=['POST'])
def read_json():
    data = request.json
    if (check_the_input(data) == False):
        
        response = make_response(
                jsonify(
                    {"message": str("CHECK_INPUT"), "severity": "danger"}
                    ),
                    400,
                )
        return response
    else:
        if datetime_valid(data["time"]) == False:
            response = make_response(
                jsonify(
                    {"message": str("CHECK_TIMESTAMP"), "severity": "danger"}
                    ),
                    400,
                )
            return response
        else:
            response = calculate_delivery_fee(data)
            return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)