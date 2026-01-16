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



if __name__ == "__main__":
    print("===test Field===")
    p1 = Potato()
    c1 = Corn()
    my_farm = Field("myFarm")

    my_farm.plant(p1)
    my_farm.plant(c1)

    for day in range(3):
        print(f'\n[Day {day+1}]')
        my_farm.water_all()
    
    my_farm.harvest()

    print(f'\nRemaining crops: {len(my_farm.crops)}')