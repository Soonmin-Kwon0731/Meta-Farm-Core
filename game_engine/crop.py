class Crop:
    def __init__(self, name, max_growth=3):
        self.name = name
        self.growth_step = 0 
        self.max_growth = max_growth

    def grow(self):
        if self.growth_step < self.max_growth:
            self.growth_step += 1
            print(f' {self.name} is growing! [Current: {self.growth_step}/{self.max_growth}]')
        else:
            print(f' {self.name} is fully grown!')

    def is_harvestable(self):
        return self.growth_step >= self.max_growth
        
    def __str__(self):
        return f'[{self.name} | {self.growth_step}/{self.max_growth}]'
    
class Potato(Crop):
    def __init__(self, max_growth=5):
        super().__init__("Potato",max_growth)
    
    def grow(self):
        if self.growth_step < self.max_growth:
            self.growth_step += 2

            if self.growth_step >= self.max_growth:
                self.growth_step = self.max_growth
                print(f' {self.name} is fully grown![Current: {self.growth_step}/{self.max_growth}]') 
            else:
                print(f' {self.name} is growing! [Current: {self.growth_step}/{self.max_growth}]')

class Corn(Crop):
    def __init__(self, max_growth=10):
        super().__init__("Corn",max_growth)

if __name__ == "__main__":
    print("=== Crop Class Test ===")
    
    potato = Potato()
    print(potato)

    potato.grow() 
    potato.grow() 
    potato.grow() 

    if potato.is_harvestable():
        print('Success! Ready to harvest ')
    else:
        print('Not ready yet...')