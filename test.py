from game_engine import Potato, Corn, Field

print("=== 🧪 Unit Test Mode: Field Test ===")

# --- 여기서부터는 아까 field.py 맨 밑에 있던 코드를 가져온 겁니다 ---
p1 = Potato() # 감자 생성
c1 = Corn()   # 옥수수 생성
test_field = Field("Test Farm") # 테스트용 밭 생성

test_field.plant(p1)
test_field.plant(c1)

print("\n--- 3일간 물주기 테스트 ---")
for day in range(3):
    test_field.water_all()

test_field.harvest()
print(f'\n[Result] 남은 작물: {len(test_field.crops)}개')


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