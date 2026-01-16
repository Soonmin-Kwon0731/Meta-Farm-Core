def show_main_menu(days, money):
    """메인 메뉴 (대분류)"""
    print("\n" + "="*40)
    print(f"   🚜 Meta-Farm [Day {days}] (Money: ${money})")
    print("="*40)
    print("1. 📊 Check Status")
    print("2. 🏪 Visit Store")
    print("3. 🚜 Go Farming")
    print("9. ❌ Exit Game")
    print("="*40)

def show_shop_menu(money):

    print("\n" + "-"*30)
    print(f"   [🏪 General Store] (Balance: ${money})")
    print("-" * 30)
    print("1. Buy Potato Seed ($10)")
    print("2. Buy Corn Seed   ($20)")
    print("3. Sell All Harvested Crops 💰")
    print("0. 🔙 Back to Main Menu")
    print("-" * 30)

def show_farming_menu():
    """농사 메뉴 (서브)"""
    print("\n" + "-"*30)
    print("   [🚜 Farming Zone]")
    print("-" * 30)
    print("1. 💧 Water All Crops (물 주기)")
    print("2. 🌾 Harvest Crops (수확해서 창고로)")
    print("0. 🔙 Back to Main Menu")
    print("-" * 30)

def show_status(field, store):
    """상태 확인"""
    print("\n" + "#"*40)
    print(f" [📊 Current Status Report]")
    print(f" 💰 Money: ${store.money}")
    print(f" 🌱 Crops: {len(field.crops)} plants")
    print(f" 📦 Inventory: {len(store.inventory)} harvested items") # 나중에 인벤토리 개념도 넣으면 좋겠죠?
    print("#" * 40)
    if len(field.crops) > 0:
        print(" [Field Details]")
        for i, crop in enumerate(field.crops, 1):
            print(f"   {i}. {crop}")
    else:
        print("   (Field is empty)")
    print("#" * 40)

def show_message(msg):
    print(f"\n🔔 [System] {msg}")