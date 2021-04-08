class District:

    def __init__(self, district : str, state : str):
        self._district = district
        self._state = state
        self._mandis = set()
    

    def add_mandi(self, mandi : str):
        self._mandis.add(mandi)

    @property
    def mandis(self):
        return list(self._mandis)
    
    @property
    def state(self):
        return self._state
    
    @property
    def district(self):
        return self._district