class Crop:

    def __init__(self, crop_name : str):
        self._crop_name = crop_name
        self._crop_varieties = set()
    
    def add_crop_variety(self, crop_variety : str):
        self._crop_varieties.add(crop_variety)
    
    @property
    def crop_varieties(self):
        return self._crop_varieties
    
    @property
    def crop_name(self):
        return self._crop_name
    