# starbuzz_demo.py
from beverage import Espresso, DarkRoast
from condiments import Mocha, Whip

if __name__ == "__main__":
    beverage = Espresso()
    print(beverage.get_description(), beverage.cost())

    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(beverage2.get_description(), beverage2.cost())
