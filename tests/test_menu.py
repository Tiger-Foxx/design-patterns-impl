# tests/test_menu.py
import sys
import os

# Ajouter le répertoire `src` au PYTHONPATH pour permettre l'import du package
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from menu_composite.menu import Menu
from menu_composite.menu_item import MenuItem
from menu_composite.waitress import Waitress


def test_specific_menu_printing(capsys):
    root = Menu("Root", "root menu")
    m = Menu("M1", "menu 1")
    it = MenuItem("I1", "item 1", True, 1.0)
    m.add(it)
    root.add(m)
    waiter = Waitress(root)
    waiter.print_specific_menu("M1")
    captured = capsys.readouterr()
    assert "M1" in captured.out or "menu 1" in captured.out
