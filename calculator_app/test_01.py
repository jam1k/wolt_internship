from calculate import app
import json

def test_input_data_cart():
    # Cart value must fail if not integer
    data = {
        "cart_value": "790", 
        "delivery_distance": 2235, 
        "number_of_items": 4, 
        "time": "2021-10-12T13:00:00Z"
    }
    response = app.test_client().post(
        '/read_json',
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
        )
    res = json.loads(response.data.decode('utf-8'))
    assert res["cart_value"] == ['must be of integer type']
    assert response.status_code == 400

def test_input_data_distance():
    # Delivery distance must fail if not integer
    data = {
        "cart_value": 790, 
        "delivery_distance": "2235", 
        "number_of_items": 4, 
        "time": "2021-10-12T13:00:00Z"
    }
    response = app.test_client().post(
        '/read_json',
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
        )
    res = json.loads(response.data.decode('utf-8'))
    assert res["delivery_distance"] == ['must be of integer type']
    assert response.status_code == 400

def test_input_data_items():
    # Items num must fail if not integer
    data = {
        "cart_value": 790, 
        "delivery_distance": 2235, 
        "number_of_items": "4", 
        "time": "2021-10-12T13:00:00Z"
    }
    response = app.test_client().post(
        '/read_json',
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
        )
    res = json.loads(response.data.decode('utf-8'))
    assert res["number_of_items"] == ['must be of integer type']
    assert response.status_code == 400

def test_input_data_timestamp():
    # Date time failure test case
    data = {
        "cart_value": 790, 
        "delivery_distance": 2235, 
        "number_of_items": 4, 
        "time": "2021-10-"
    }
    response = app.test_client().post(
        '/read_json',
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
        )
    res = json.loads(response.data.decode('utf-8'))
    assert res["time"] == ['Must be a date in ISO format']
    assert response.status_code == 400

def test_input_data_negative_cart():
    # test cart_value < 0
    data = {
        "cart_value": -500, 
        "delivery_distance": 2235, 
        "number_of_items": 4, 
        "time": "2021-10-12T13:00:00Z"
    }
    response = app.test_client().post(
        '/read_json',
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
        )
    res = json.loads(response.data.decode('utf-8'))
    assert res["cart_value"] == ['min value is 1']
    assert response.status_code == 400

def test_input_data_negative_distance():
    # test delivery_distance < 0
    data = {
        "cart_value": 1000, 
        "delivery_distance": -2235, 
        "number_of_items": 4, 
        "time": "2021-10-12T13:00:00Z"
    }
    response = app.test_client().post(
        '/read_json',
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
        )
    res = json.loads(response.data.decode('utf-8'))
    assert res["delivery_distance"] == ['min value is 1']
    assert response.status_code == 400

def test_input_data_negative_items():
    # test number_of_items < 0
    data = {
        "cart_value": 1000, 
        "delivery_distance": 2235, 
        "number_of_items": -4, 
        "time": "2021-10-12T13:00:00Z"
    }
    response = app.test_client().post(
        '/read_json',
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
        )
    res = json.loads(response.data.decode('utf-8'))
    assert res["number_of_items"] == ['min value is 1']
    assert response.status_code == 400

def test_input_data_cart_null():
    # test cart_value = 0
    data = {
        "cart_value": 0, 
        "delivery_distance": 2235, 
        "number_of_items": 4, 
        "time": "2021-10-12T13:00:00Z"
    }
    response = app.test_client().post(
        '/read_json',
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
        )
    res = json.loads(response.data.decode('utf-8'))
    assert res["cart_value"] == ['min value is 1']
    assert response.status_code == 400

def test_input_data_distance_null():
    # test delivery_distance = 0
    data = {
        "cart_value": 1000, 
        "delivery_distance": 0, 
        "number_of_items": 4, 
        "time": "2021-10-12T13:00:00Z"
    }
    response = app.test_client().post(
        '/read_json',
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
        )
    res = json.loads(response.data.decode('utf-8'))
    assert res["delivery_distance"] == ['min value is 1']
    assert response.status_code == 400

def test_input_data_items_null():
    # test number_of_items = 0
    data = {
        "cart_value": 1000, 
        "delivery_distance": 1000, 
        "number_of_items": 0, 
        "time": "2021-10-12T13:00:00Z"
    }
    response = app.test_client().post(
        '/read_json',
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
        )
    res = json.loads(response.data.decode('utf-8'))
    assert res["number_of_items"] == ['min value is 1']
    assert response.status_code == 400

def test_response():
    # test server response 200 for the correct data input
    data = {
        "cart_value": 790, 
        "delivery_distance": 2235, 
        "number_of_items": 4, 
        "time": "2021-10-12T13:00:00Z"
    }
    response = app.test_client().post(
        '/read_json',
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
        )
    assert response.status_code == 200

def test_cart_value():
    # testing values that the delivery fee is 710 and output is int
    data = {
        "cart_value": 790, 
        "delivery_distance": 2235, 
        "number_of_items": 4, 
        "time": "2021-10-12T13:00:00Z"
    }
    response = app.test_client().post(
        '/read_json',
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
        )
    res = json.loads(response.data.decode('utf-8'))
    assert type(res["delivery_fee"]) is int
    assert res["delivery_fee"] == 710 #answer given in the task
    assert response.status_code == 200

def test_distance1499():
    # testing distance 1499
    data = {
        "cart_value": 1000, 
        "delivery_distance": 1499, 
        "number_of_items": 4, 
        "time": "2021-10-12T13:00:00Z"
    }
    response = app.test_client().post(
        '/read_json',
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
        )
    res = json.loads(response.data.decode('utf-8'))
    assert type(res["delivery_fee"]) is int
    assert res["delivery_fee"] == 300
    assert response.status_code == 200

def test_distance1500():
    # testing distance 1500
    data = {
        "cart_value": 1000, 
        "delivery_distance": 1500, 
        "number_of_items": 4, 
        "time": "2021-10-12T13:00:00Z"
    }
    response = app.test_client().post(
        '/read_json',
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
        )
    res = json.loads(response.data.decode('utf-8'))
    assert type(res["delivery_fee"]) is int
    assert res["delivery_fee"] == 300
    assert response.status_code == 200

def test_distance1501():
    # testing distance 1501
    data = {
        "cart_value": 1000, 
        "delivery_distance": 1501, 
        "number_of_items": 4, 
        "time": "2021-10-12T13:00:00Z"
    }
    response = app.test_client().post(
        '/read_json',
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
        )
    res = json.loads(response.data.decode('utf-8'))
    assert type(res["delivery_fee"]) is int
    assert res["delivery_fee"] == 400
    assert response.status_code == 200

def test_num_items5():
    # testing items ordered = 5, distance is taken to be 1000
    data = {
        "cart_value": 1000, 
        "delivery_distance": 999, 
        "number_of_items": 5, 
        "time": "2021-10-12T13:00:00Z"
    }
    response = app.test_client().post(
        '/read_json',
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
        )
    res = json.loads(response.data.decode('utf-8'))
    assert type(res["delivery_fee"]) is int
    assert res["delivery_fee"] == 250 #2 euro for 1000m and 50 cents
    assert response.status_code == 200

def test_num_items10():
    # testing items ordered = 10
    data = {
        "cart_value": 1000, 
        "delivery_distance": 999, 
        "number_of_items": 10, 
        "time": "2021-10-12T13:00:00Z"
    }
    response = app.test_client().post(
        '/read_json',
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
        )
    res = json.loads(response.data.decode('utf-8'))
    assert type(res["delivery_fee"]) is int
    assert res["delivery_fee"] == 500 #2 euro for 1000m and 300 cents
    assert response.status_code == 200

def test_num_items13():
    # testing items ordered = 13
    data = {
        "cart_value": 1000, 
        "delivery_distance": 999, 
        "number_of_items": 13, 
        "time": "2021-10-12T13:00:00Z"
    }
    response = app.test_client().post(
        '/read_json',
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
        )
    res = json.loads(response.data.decode('utf-8'))
    assert type(res["delivery_fee"]) is int
    assert res["delivery_fee"] == 770 #2 euro for 1000m and 570 cents ((9 * 50 cents) + 1,20€)
    assert response.status_code == 200

def test_num_surcharge():
    # testing surcharge calculated correctly surcharge = 210
    data = {
        "cart_value": 790, 
        "delivery_distance": 999, 
        "number_of_items": 4, 
        "time": "2021-10-12T13:00:00Z"
    }
    response = app.test_client().post(
        '/read_json',
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
        )
    res = json.loads(response.data.decode('utf-8'))
    assert type(res["delivery_fee"]) is int
    assert res["delivery_fee"] == 410 #2 euro for 1000m and 210 cents surcharge
    assert response.status_code == 200


def test_null_surcharge():
    # testing surcharge calculated correctly surcharge (if cart_value = 1000, surcharge = 0)
    data = {
        "cart_value": 1000, 
        "delivery_distance": 999, 
        "number_of_items": 4, 
        "time": "2021-10-12T13:00:00Z"
    }
    response = app.test_client().post(
        '/read_json',
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
        )
    res = json.loads(response.data.decode('utf-8'))
    assert type(res["delivery_fee"]) is int
    assert res["delivery_fee"] == 200 #2 euro for 1000m and 0 cents surcharge
    assert response.status_code == 200


def test_fee_max():
    # delivery fee cannot be more than 15 euro
    data = {
        "cart_value": 1000, 
        "delivery_distance": 999999999999999, 
        "number_of_items": 4, 
        "time": "2021-10-12T13:00:00Z"
    }
    response = app.test_client().post(
        '/read_json',
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
        )
    res = json.loads(response.data.decode('utf-8'))
    assert type(res["delivery_fee"]) is int
    assert res["delivery_fee"] == 1500 #max fee 15 euro
    assert response.status_code == 200


def test_free_delivery():
    # delivery fee cannot be more than 15 euro
    data = {
        "cart_value": 10000, 
        "delivery_distance": 999999999999999, 
        "number_of_items": 4, 
        "time": "2021-10-12T13:00:00Z"
    }
    response = app.test_client().post(
        '/read_json',
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
        )
    res = json.loads(response.data.decode('utf-8'))
    assert type(res["delivery_fee"]) is int
    assert res["delivery_fee"] == 0 #free delivery
    assert response.status_code == 200


def test_fryday_rush():
    # during Friday rush hours delivery should be multiplied by 1.2
    data = {
        "cart_value": 790, 
        "delivery_distance": 2235, 
        "number_of_items": 4, 
        "time": "2023-01-13T15:01:00Z"
    }
    response = app.test_client().post(
        '/read_json',
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
        )
    res = json.loads(response.data.decode('utf-8'))
    assert type(res["delivery_fee"]) is float
    assert res["delivery_fee"] == 852 # 710 * 1.2 = 852
    assert response.status_code == 200