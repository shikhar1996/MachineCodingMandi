class CropVariety:

    def __init__(self, crop_variety : str):
        self._crop_variety = crop_variety
    
    @property
    def crop_variety(self):
        return self._crop_variety