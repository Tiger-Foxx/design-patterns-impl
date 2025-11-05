# menu_component.py
from abc import ABC, abstractmethod
from typing import Any, Dict, Iterator


class MenuComponent(ABC):
    """Abstraction commune pour Menu et MenuItem."""

    def add(self, component: "MenuComponent") -> None:
        raise NotImplementedError

    def remove(self, component: "MenuComponent") -> None:
        raise NotImplementedError

    def get_child(self, i: int) -> "MenuComponent":
        raise NotImplementedError

    def get_name(self) -> str:
        raise NotImplementedError

    def get_description(self) -> str:
        raise NotImplementedError

    def get_price(self) -> float:
        raise NotImplementedError

    def is_vegetarian(self) -> bool:
        raise NotImplementedError

    def print(self, indent: int = 0) -> None:
        raise NotImplementedError

    def create_iterator(self) -> Iterator["MenuComponent"]:
        """Retourne un itérateur sur les enfants (pour les composites).
        Doit lever ou retourner un itérateur vide pour les feuilles."""
        raise NotImplementedError

    def to_dict(self) -> Dict[str, Any]:
        raise NotImplementedError
