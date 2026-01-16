import sys
from game_engine import Potato, Corn, Field

def print_menu():
    print("\n" + "="*40)
    print("   🚜 Meta-Farm Controller (V1.0)   ")
    print("="*40)
    print("1. Plant Potato (Fast Growth) 🥔")
    print("2. Plant Corn (High Value) 🌽")
    print("3. Water All Crops 💧")
    print("4. Harvest Crops 🌾")
    print("5. Check Farm Status 👀")
    print("9. Exit Game ❌")
    print("="*40)

def main():
    # Initialize Field
    my_farm = Field("My Weekend Farm")
    
    # Game Loop
    while True:
        print_menu()
        choice = input("Select an option (Input number): ")

        if choice == '1':
            # Dynamic Instantiation: Create a new Potato object
            new_crop = Potato() 
            my_farm.plant(new_crop)
            
        elif choice == '2':
            # Create a new Corn object
            new_crop = Corn()
            my_farm.plant(new_crop)
            
        elif choice == '3':
            # Grow all crops
            my_farm.water_all()
            
        elif choice == '4':
            # Try to harvest
            my_farm.harvest()
            
        elif choice == '5':
            # Show status
            count = len(my_farm.crops)
            print(f"\n[System] You have {count} crops in the field.")
            
            # (Optional) Show details of each crop
            if count > 0:
                print("--- Crop List ---")
                for c in my_farm.crops:
                    print(c) 

        elif choice == '9':
            print("\nExiting Meta-Farm... See you next time! 👋")
            sys.exit() # Terminate program
            
        else:
            print("\n[Error] Invalid input. Please try again.")

if __name__ == "__main__":
    main()