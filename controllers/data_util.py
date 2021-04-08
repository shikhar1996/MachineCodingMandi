from models.crop import Crop
from models.crop_variety import CropVariety
from models.mandi import Mandi
from models.price import Price
from models.district import District
from collections import defaultdict

# global instances of created objects
mandi_instances = {}
crop_instances = {}
crop_variety_instances = {}
price_instances = {}
district_instances = {}

# Input data is in the form of list
def update_data(input_data : list[str]):
    try:
        for data in input_data:
            state, district, mandi, crop, crop_variety, date, price = data.split(', ')

            # check for the instance of mandi in mandi_instances else create
            if (mandi, state, district) in mandi_instances:
                mandi_instance = mandi_instances[(mandi, state, district)]
            else:
                mandi_instance = Mandi(mandi, state, district)
                mandi_instances[(mandi, state, district)] = mandi_instance

            # add crop for the particular mandi
            mandi_instance.add_crop(crop)

            # check for the instance of crop in crop_instances else create
            if crop in crop_instances:
                crop_instance = crop_instances[crop]
            else:
                crop_instance = Crop(crop)
                crop_instances[crop] = crop_instance

            # add crop_variety for the crop
            crop_instance.add_crop_variety(crop_variety)

            # check for the instance of crop_variety in crop_variety_instances else create
            if crop_variety in crop_variety_instances:
                crop_variety_instance = crop_variety_instances[crop_variety]
            else:
                crop_variety_instance = CropVariety(crop_variety)
                crop_variety_instances[crop_variety] = crop_variety_instance
            
            # check for the instance of date, price in price_instance else create
            if (mandi, crop, crop_variety) in price_instances:
                price_instance = price_instances[(mandi, crop, crop_variety)]
            else:
                price_instance = Price(mandi, crop, crop_variety)
                price_instances[(mandi, crop, crop_variety)] = price_instance
            
            # add date and price for a paticular mandi, crop and crop_variety
            price_instance.add_date_price(date, price)
            
            # check for the instance of mandi in mandi_instance else create
            if (district, state) in district_instances:
                district_instance = district_instances[(district, state)]
            else:
                district_instance = District(district, state)
                district_instances[(district, state)] = district_instance
            
            # add mandi in district
            district_instance.add_mandi(mandi)

    except Exception as e:
        print(e)
        raise Exception(e)
    
    print("Data successfully updated")
    return 1

def get_mandis(state : str, district : str):
    mandis = district_instances[(district, state)].mandis
    return mandis

def get_crop_varieties(crop: str):
    crop_varieties = crop_instances[crop].crop_varieties
    return crop_varieties

def get_date_price(mandi : str, crop : str, crop_variety: str):
    date_price = price_instances[(mandi, crop, crop_variety)].date_price
    return date_price