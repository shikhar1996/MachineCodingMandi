class Mandi:

    def __init__(self, name : str, state : str, district : str):
        self._name = name
        self._state = state
        self._district = district
        self._crops = set()
    
    def add_crop(self, crop : str):
        self._crops.add(crop)

    @property
    def crops(self):
        return self._crops
    
    @property
    def name(self):
        return self._name
    
    @property
    def state(self):
        return self._state
    
    @property
    def district(self):
        return self._district