class Store:
    def __init__(self, start_money=100):
        self.money = start_money
        self.crop_prices = {
            "Potato": 10,
            "Corn": 20
        }

        self.sell_prices={
            "Potato": 30,
            "Corn": 60
        }

    def buy_crop(self, crop_name):
        """
        Attempts to buy a crop seed.
        Returns True if successful, False if not enough money.
        """
        price = self.crop_prices[crop_name]

        if self.money >= price:
            self.money -= price
            print(f"💰 You Purchased {crop_name} seed for ${price}. (Balance: ${self.money})")
            return True
        else:
            print(f"❌ Not enough money! (Cost: ${price}, Balance: ${self.money})")
            return False
        
    def sell_crop(self, crop_name):
        """
        Sells a harvested crop and adds money.
        """
        price = self.sell_prices.get(crop_name, 0)
        
        if price > 0:
            self.money += price
            print(f"💵 You sold {crop_name} for ${price}. (Balance: ${self.money})")
        else:
            print(f"⚠️ [Store] We don't buy {crop_name}.")