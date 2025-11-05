import sys
import os

# ajouter src au PYTHONPATH
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from menu_composite.menu import Menu
from menu_composite.menu_item import MenuItem
from menu_composite.waitress import Waitress


def run():
    root = Menu("Root", "root menu")
    m = Menu("M1", "menu 1")
    it = MenuItem("I1", "item 1", True, 1.0)
    m.add(it)
    root.add(m)
    waiter = Waitress(root)
    waiter.print_specific_menu("M1")


if __name__ == '__main__':
    run()
