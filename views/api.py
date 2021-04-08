from controllers.data_util import update_data, get_mandis, get_crop_varieties, get_date_price
from controllers.date_util import get_date_from_string
from constants.constants import TODAY
import json

"""
Input:
    data: type dict
    parameters: state, district, crop

Output:
    latest_price: type JSON
"""
def get_latest_price(data : dict):

    # list to store prices sorted by date for mandi and crop variety
    latest_prices_by_mandi = []

    try:
        # get parameters from request body
        state, district, crop = data['state'], data['district'], data['crop']
    
        # get all the mandis for a given district in a state
        mandis = get_mandis(state, district)

        # get all the crop varieties for a particular crop
        crop_varieties = get_crop_varieties(crop)

        # generate all possible combination for mandi and crop variety
        all_possible = [(mandi, crop_variety) for mandi in mandis for crop_variety in crop_varieties]

        for mandi, crop_variety in all_possible:
            output = {}
            output['mandi'] = mandi
            output['crop'] = crop
            output['crop_variety'] = crop_variety
            prices = []
            price_list = get_date_price(mandi, crop, crop_variety)

            # if there are price list is not empty add prices
            if price_list:
                temp = {}
                for date, price in price_list:
                    temp['date'] = date
                    temp['price'] = price
                    prices.append(temp)
                output['prices'] = prices
                latest_prices_by_mandi.append(output)
    
    except Exception as e:
        print(e)
        raise Exception(e)
    
    return json.dumps(latest_prices_by_mandi)

"""
Input:
    data: type dict
    parameters: state, district, mandi, crop, crop_variety, points, days

Output:
    price_trend: type JSON
"""
def get_price_trend(data : dict) -> dict:
    try:
        # get parameters from request body
        state, district, mandi, crop, crop_variety, total_points, within_days = data['state'], data['district'], data['mandi'], data['crop'], data['crop_variety'], data['points'], data['days']
        # get price list by mandi, crop, crop_variety
        price_list = get_date_price(mandi, crop, crop_variety)

        # structure to store trend
        price_trend = {}
        price_trend['state'] = state
        price_trend['mandi'] = mandi
        price_trend['district'] = district
        price_trend['crop'] = crop
        price_trend['crop_variety'] = crop_variety
        filtered_price_list = []

        # iterate over date price tuple
        for date, price in price_list:
            date_price_data = {}
            date_object = get_date_from_string(date)

            # only get previous x datapoints that is within y days
            if total_points > 0 and  (TODAY-date_object).days <= within_days:
                date_price_data['date'] = date
                date_price_data['price'] = price
                filtered_price_list.append(date_price_data)
                total_points -= 1
            else:
                break

        price_trend['prices'] = filtered_price_list

    except Exception as e:
        print(e)
        raise Exception(e)
    
    return json.dumps(price_trend)
            



