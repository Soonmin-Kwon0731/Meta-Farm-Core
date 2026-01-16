from .crop import Potato, Corn

class Field:
    def __init__(self,name):
        self.name = name
        self.crops = []
    
    def plant(self,crop_name):
        self.crops.append(crop_name)
        print(f'[{crop_name}] has just been planted!')
    
    def water_all(self):
        print(f'\n--- Watering [{self.name}] ---')
        for crop in self.crops:
            crop.grow()
    
    def harvest(self):
        for crop in self.crops[:]:
            if crop.is_harvestable():
                print(f'[{crop.name}] is harvested!')
                self.crops.remove(crop)



