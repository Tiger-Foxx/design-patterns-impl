# waitress.py
from typing import Optional
from .menu_component import MenuComponent
from .menu import Menu
from .composite_iterator import CompositeIterator


class Waitress:
    """Serveur (attitude 'serveur de restaurant') — client qui utilise Composite
    et Iterator. Implémente :
      - print_menu() : affiche tout
      - print_vegetarian() : affiche les items végétariens
      - print_specific_menu(name) : affiche le menu (sous-arbre) portant ce nom
    """

    def __init__(self, all_menus: Menu):
        self._all_menus = all_menus

    def print_menu(self) -> None:
        self._all_menus.print()

    def print_vegetarian(self) -> None:
        print("VEGETARIAN ITEMS:")
        iterator = CompositeIterator(self._all_menus.create_iterator())
        for component in iterator:
            # seuls les MenuItem ont is_vegetarian() de sens
            try:
                if component.is_vegetarian():
                    component.print(2)
            except Exception:
                # ignorer les composites
                pass

    def find_menu_by_name(self, name: str) -> Optional[MenuComponent]:
        """Recherche récursive d'un Menu (composite) donné son nom."""
        # On peut utiliser l'itérateur composite pour parcourir tout l'arbre
        iterator = CompositeIterator(self._all_menus.create_iterator())
        for component in iterator:
            try:
                if component.get_name() == name:
                    return component
            except Exception:
                pass
        return None

    def print_specific_menu(self, name: str) -> None:
        """Méthode demandée : affiche un menu spécifique (sous-arbre).
        Si le nom correspond à un Menu, affiche sa structure. S'il correspond
        à un MenuItem, affiche l'item seul."""
        found = self.find_menu_by_name(name)
        if not found:
            print(f"Menu '{name}' introuvable.")
            return
        # si c'est un menu (composite) -> utiliser print() pour afficher récursivement
        try:
            # S'il a create_iterator -> composite -> print complet
            _ = found.create_iterator()
            found.print()
        except Exception:
            # feuille (MenuItem) -> print seul
            found.print()
