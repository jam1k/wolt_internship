from dateutil import parser
from datetime import time, datetime
from cerberus import Validator

def datetime_test(field, value, error):
    try:
        datetime.fromisoformat(value.replace('Z', '+00:00'))
    except:
        error(field, "Must be a date in ISO format")
    
def check_the_input(data):
    # Function is used to check the input data 
    # Made an assumption, that cart value, distance and number of items has to be >= 1
    schema = {
        "cart_value": {'type': 'integer', 'required': True, 'min': 1}, 
        "delivery_distance": {'type': 'integer', 'required': True, 'min': 1}, 
        "number_of_items": {'type': 'integer', 'required': True, 'min': 1}, 
        "time": {'check_with': datetime_test, 'required': True}
        }
    v = Validator(schema)
    v.validate(data)
    return v.errors

def add_surcharge(cart_value: int):
    # If the cart value is less than 10€, a small order surcharge is added to the delivery price. 
    # The surcharge is the difference between the cart value and 10€. 
    # For example if the cart value is 8.90€, the surcharge will be 1.10€.
    return max(0, 1000 - cart_value)

def delivery_based_on_distance(distance: int):
    # A delivery fee for the first 1000 meters (=1km) is 2€. 
    # If the delivery distance is longer than that, 1€ is added for every additional 500 meters 
    # that the courier needs to travel before reaching the destination.
    base_fee = 200
    if distance <= 1000:
        delivery_fee = 0
    else:
        additional_meters = distance - 1000
        if additional_meters % 500 != 0:
            delivery_fee = (additional_meters // 500) * 100 + 100
        else:
            delivery_fee = (additional_meters // 500) * 100
    return delivery_fee + base_fee

def delivery_based_on_items(number_of_items: int):
    # If the number of items is five or more, an additional 50 cent surcharge is added for each item above five. 
    # An extra "bulk" fee applies for more than 12 items of 1,20€
    i = 0
    item_fee = 0
    while i <= number_of_items:
        if i < 5:
            item_fee = 0
        else:
            item_fee += 50
        i += 1
    if number_of_items >= 13:
        item_fee += 120
        
    return item_fee

def is_friday_rush(timestamp: str):
    # to convert UTC string to datetime object dateutil parser was used
    # pip install python-dateutil
    date = parser.parse(timestamp)
    weekday = date.weekday()
    if weekday != 4:
        return False
    else:
        start = time(hour = 15, minute = 00, second = 00)
        end = time(hour=17, minute=00, second=00)
        if date.time() >= start and date.time() <= end:
            return True

def calculate_delivery_fee(data: dict):
    out_data = {}
    max_delivery_fee = 1500

    # The delivery is free (0€) when the cart value is equal or more than 100€.
    if data["cart_value"] >= 10000:
        out_data['delivery_fee'] = 0
        return out_data
    surcharge = add_surcharge(data["cart_value"])
    distance_fee = delivery_based_on_distance(data["delivery_distance"])
    items_fee = delivery_based_on_items(data["number_of_items"])
    delivery_fee = surcharge + distance_fee + items_fee
    if is_friday_rush(data["time"]):
        delivery_fee *= 1.2
    if delivery_fee <= max_delivery_fee:
        out_data['delivery_fee'] = delivery_fee
    else:
        out_data['delivery_fee'] = max_delivery_fee
    return out_data

if __name__ == "__main__":
    data = {
        "cart_value": "0", 
        "delivery_distance": 999, 
        "number_of_items": 4, 
        "time": "2021-10-12T13:00:00Z"
    }
    check_the_input(data)
    print(calculate_delivery_fee(data))