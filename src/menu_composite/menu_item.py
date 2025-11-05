# menu_item.py
from typing import Dict, Any
from .menu_component import MenuComponent


class MenuItem(MenuComponent):
    def __init__(self, name: str, description: str, vegetarian: bool, price: float):
        self._name = name
        self._description = description
        self._vegetarian = vegetarian
        self._price = price

    def get_name(self) -> str:
        return self._name

    def get_description(self) -> str:
        return self._description

    def get_price(self) -> float:
        return self._price

    def is_vegetarian(self) -> bool:
        return self._vegetarian

    def print(self, indent: int = 0) -> None:
        pad = " " * indent
        veg = " (v)" if self._vegetarian else ""
        print(f"{pad}{self._name}{veg} — {self._price:.2f} : {self._description}")

    def create_iterator(self):
        # feuille : aucun enfant -> itérateur vide
        return iter([])

    def to_dict(self) -> Dict[str, Any]:
        return {
            "type": "MenuItem",
            "name": self._name,
            "description": self._description,
            "vegetarian": self._vegetarian,
            "price": self._price,
        }
