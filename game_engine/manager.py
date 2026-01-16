from .crop import Potato, Corn
from . import ui

def run_shop_mode(farm, store, inventory):
    """2. 상점 모드 (서브 루프)"""
    while True:
        ui.show_shop_menu(store.money)
        choice = input("Select Shop Option: ")

        if choice == '1': # 감자 구매
            if store.buy_crop("Potato"):
                farm.plant(Potato())
        
        elif choice == '2': # 옥수수 구매
            if store.buy_crop("Corn"):
                farm.plant(Corn())

        elif choice == '3': # 판매 (현재 밭에 있는 게 아니라, 수확해서 손에 든 걸 팔아야 함)
            # 💡 중요: 지금 구조상 '수확한 작물'을 어딘가 임시 저장해야 합니다.
            # 일단은 밭에 있는 걸 바로 파는 게 아니라, 
            # 'Farming' 메뉴에서 수확한 것들을 'inventory' 리스트에 담는 로직이 필요합니다.
            # (아래 main 함수에서 inventory 리스트를 새로 만듭니다)
            if len(inventory) > 0:
                count = 0
                total_earnings = 0 # (선택사항) 총 얼마 벌었는지 계산
                
                print("\n--- 💰 Selling Items ---")
                for crop in inventory:
                    # store.sell_crop 함수가 돈을 올려줍니다.
                    store.sell_crop(crop.name)
                    count += 1
                
                # 다 팔았으니 가방을 비웁니다.
                inventory.clear()
                ui.show_message(f"Deal Complete! Sold {count} items.")
            else:
                ui.show_message("Inventory is empty! Go harvest some crops first.")

        elif choice == '0': # 뒤로 가기
            return # 함수를 끝내면 메인 메뉴로 돌아갑니다.
        
        else:
            ui.show_message("Invalid option.")

def run_farming_mode(farm, inventory):
    """3. 농사 모드 (서브 루프)"""
    while True:
        ui.show_farming_menu()
        choice = input("Select Farming Option: ")

        if choice == '1': # 물 주기
            farm.water_all()
        
        elif choice == '2': # 수확하기
            # 수확한 작물들을 받아서 인벤토리(가방)에 넣습니다.
            harvested = farm.harvest()
            if len(harvested) > 0:
                inventory.extend(harvested) # 가방에 추가
                ui.show_message(f"{len(harvested)} crops moved to Inventory! Go to Store to sell.")
            else:
                ui.show_message("Nothing to harvest yet.")

        elif choice == '0': # 뒤로 가기
            return
        
        else:
            ui.show_message("Invalid option.")
