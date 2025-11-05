# menu.py
from typing import List, Dict, Any, Iterator
from .menu_component import MenuComponent


class Menu(MenuComponent):
    def __init__(self, name: str, description: str):
        self._name = name
        self._description = description
        self._children: List[MenuComponent] = []

    def add(self, component: MenuComponent) -> None:
        self._children.append(component)

    def remove(self, component: MenuComponent) -> None:
        self._children.remove(component)

    def get_child(self, i: int) -> MenuComponent:
        return self._children[i]

    def get_name(self) -> str:
        return self._name

    def get_description(self) -> str:
        return self._description

    def print(self, indent: int = 0) -> None:
        pad = " " * indent
        print(f"{pad}{self._name.upper()} : {self._description}")
        for c in self._children:
            c.print(indent + 2)

    def create_iterator(self) -> Iterator[MenuComponent]:
        # retourne un itérateur Python sur la liste des enfants
        return iter(self._children)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "type": "Menu",
            "name": self._name,
            "description": self._description,
            "children": [c.to_dict() for c in self._children],
        }
