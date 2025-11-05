# demo.py
from menu import Menu
from menu_item import MenuItem
from waitress import Waitress

def build_sample_menu() -> Menu:
    all_menus = Menu("All Menus", "Root of all menus")
    pancake = Menu("Pancake House Menu", "Breakfast")
    diner = Menu("Diner Menu", "Lunch")
    cafe = Menu("Cafe Menu", "Dinner")
    dessert = Menu("Dessert Menu", "Desserts")

    pancake.add(MenuItem("Blueberry Pancake", "Pancakes with fresh blueberries", True, 3.99))
    pancake.add(MenuItem("Regular Pancake", "Classic pancake with syrup", True, 2.99))

    diner.add(MenuItem("BLT", "Bacon lettuce tomato sandwich", False, 5.99))
    diner.add(MenuItem("Veggie Burger", "Burger with lettuce and tomato", True, 7.99))
    diner.add(dessert)

    cafe.add(MenuItem("Veggie Salad", "Fresh salad", True, 4.99))

    dessert.add(MenuItem("Apple Pie", "Apple pie with icecream", True, 1.99))

    all_menus.add(pancake)
    all_menus.add(diner)
    all_menus.add(cafe)
    return all_menus

if __name__ == "__main__":
    root = build_sample_menu()
    waitress = Waitress(root)

    print("\n--- Affichage complet du menu (root) ---")
    waitress.print_menu()

    print("\n--- Affichage des éléments végétariens ---")
    waitress.print_vegetarian()

    print("\n--- Affichage d'un menu spécifique : 'Diner Menu' ---")
    waitress.print_specific_menu("Diner Menu")

    print("\n--- Affichage d'un item spécifique (par nom exact) : 'Apple Pie' ---")
    waitress.print_specific_menu("Apple Pie")
