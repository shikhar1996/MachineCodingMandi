from views.api import get_latest_price, get_price_trend
from controllers.data_util import update_data
import json

global_input_data = [
'Maharashtra, Nagpur, ABC, Tomato, Hybrid, 2021-04-07, 400',
'Maharashtra, Nagpur, ABC, Tomato, Country, 2021-04-07, 450',
'Maharashtra, Nagpur, ABC, Tomato, Hybrid, 2021-04-08, 450',
'Maharashtra, Nagpur, ABC, Tomato, Country, 2021-04-08, 500',
'Maharashtra, Nagpur, XYZ, Tomato, Hybrid, 2021-04-07, 450',
'Maharashtra, Nagpur, XYZ, Tomato, Country, 2021-04-07, 500',
]

latest_price = {
    'state' : 'Maharashtra',
    'district' : 'Nagpur',
    'crop' : 'Tomato'
}

price_trend = {
    'state' : 'Maharashtra',
    'district' : 'Nagpur',
    'mandi' : 'ABC',
    'crop' : 'Tomato',
    'crop_variety' : 'Hybrid',
    'points' : 2,
    'days' : 1
}


def test_update_data():
    assert update_data(global_input_data) == 1

def test_get_latest_price():
    print(get_latest_price(latest_price))
    # assert json.loads(get_latest_price(latest_price)) == [{"mandi": "ABC", "crop": "Tomato", "crop_variety": "Country", "prices": [{"date": "2021-04-07", "price": "450"}, {"date": "2021-04-07", "price": "450"}]}, {"mandi": "ABC", "crop": "Tomato", "crop_variety": "Hybrid", "prices": [{"date": "2021-04-07", "price": "400"}, {"date": "2021-04-07", "price": "400"}]}, {"mandi": "XYZ", "crop": "Tomato", "crop_variety": "Country", "prices": [{"date": "2021-04-07", "price": "500"}]}, {"mandi": "XYZ", "crop": "Tomato", "crop_variety": "Hybrid", "prices": [{"date": "2021-04-07", "price": "450"}]}]

def test_get_price_trend():
    print(get_price_trend(price_trend))
    assert json.loads(get_price_trend(price_trend)) == {"state": "Maharashtra", "mandi": "ABC", "district": "Nagpur", "crop": "Tomato", "crop_variety": "Hybrid", "prices": [{"date": "2021-04-08", "price": "450"}, {"date": "2021-04-07", "price": "400"}]}
    
    


