class Crop:
    def __init__(self, name, max_growth = 3):
        self.name = name
        self.growth_step = 0
        self.max_growth = max_growth

    def grow(self):
        if self.growth_step < self.max_growth:
            self.growth_step += 1
            print(f' 현재 성장치 : {self.growth_step}')

    def is_harvestable(self):
        if self.growth_step == self.max_growth:
            return True
        else:
            return False
        
    def __str__(self):
        return f'[{self.name} | {self.growth_step}/{self.max_growth}]'
    


if __name__ == "__main__":
    print("=== Crop class test ===")
    my_crop = Crop('테스트 콩',2)
    print(my_crop)

    my_crop.grow()
    my_crop.grow()

    if my_crop.is_harvestable():
        print('테스트 성공! 수확 가능합니다')
    else:
        print('테스트 실패... 아직 안자랐습니다.')
