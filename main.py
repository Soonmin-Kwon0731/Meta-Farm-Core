import sys
from game_engine import Field, Store, ui, run_farming_mode, run_shop_mode

def main():
    my_farm = Field("Weekend Farm")
    my_store = Store(start_money=100)
    my_inventory = [] 
    my_store.inventory = my_inventory 
    days = 1 

    while True:
        # 1. 메인 메뉴 보여주기
        ui.show_main_menu(days, my_store.money)
        choice = input("Select Main Option: ")

        if choice == '1': # 상태 확인
            ui.show_status(my_farm, my_store)
            input("Press Enter to continue...") # 바로 넘어가지 않게 잠시 멈춤

        elif choice == '2': # 상점 모드로 이동
            # 상점 모드 함수를 실행 (갔다가 돌아옴)
            # 여기서는 인벤토리 판매 로직을 따로 구현해야 합니다.
            run_shop_mode(my_farm, my_store,my_inventory)

        elif choice == '3': # 농사 모드로 이동
            run_farming_mode(my_farm, my_inventory)
            days += 1 # 농사짓고 나오면 하루가 지남 (선택사항)

        elif choice == '9':
            ui.show_message("See you next time!")
            sys.exit()

        else:
            ui.show_message("Wrong input.")

if __name__ == "__main__":
    main()