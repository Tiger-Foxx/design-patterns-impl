# composite_iterator.py
from typing import Iterator, List
from .menu_component import MenuComponent


class CompositeIterator:
    """Itérateur qui parcourt un arbre Menu/MenuItem en profondeur (DFS) sans
    exposer la structure interne au client.
    Implémentation classique : pile d'itérateurs."""

    def __init__(self, iterator):
        # la pile contient des itérateurs (sur listes d'enfants)
        self.stack: List[Iterator] = [iterator]

    def __iter__(self):
        return self

    def __next__(self) -> MenuComponent:
        while self.stack:
            try:
                component = next(self.stack[-1])
                # si component a des enfants (composite) on empile son iterator
                try:
                    child_iter = component.create_iterator()
                    # empile l'itérateur des enfants (peut être vide)
                    self.stack.append(iter(child_iter))
                except Exception:
                    # feuilles : create_iterator peut lever NotImplemented; on ignore
                    pass
                return component
            except StopIteration:
                # itérateur courant fini -> dépile
                self.stack.pop()
        raise StopIteration
