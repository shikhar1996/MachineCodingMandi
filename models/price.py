from collections import deque
class Price:

    def __init__(self, mandi : str, crop : str, crop_variety : str):
        self._mandi = mandi
        self._crop = crop
        self._crop_variety = crop_variety
        self._date_price = deque()
    
    def add_date_price(self, date : str, price : str):
        self._date_price.appendleft((date, price))

    @property
    def date_price(self):
        return self._date_price
    
    @property
    def mandi(self):
        return self._mandi
    
    @property
    def crop(self):
        return self._crop
    
    @property
    def crop_variety(self):
        return self._crop_variety