# beverage.py
from abc import ABC, abstractmethod

class Beverage(ABC):
    def __init__(self):
        self.description = "Unknown Beverage"

    def get_description(self) -> str:
        return self.description

    @abstractmethod
    def cost(self) -> float:
        pass

class Espresso(Beverage):
    def __init__(self):
        super().__init__()
        self.description = "Espresso"

    def cost(self) -> float:
        return 1.99

class DarkRoast(Beverage):
    def __init__(self):
        super().__init__()
        self.description = "Dark Roast"

    def cost(self) -> float:
        return 0.99
