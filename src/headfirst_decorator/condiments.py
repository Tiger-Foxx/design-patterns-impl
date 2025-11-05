# condiments.py
from beverage import Beverage
from abc import ABC, abstractmethod

class CondimentDecorator(Beverage, ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

class Mocha(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self) -> str:
        return self.beverage.get_description() + ", Mocha"

    def cost(self) -> float:
        return self.beverage.cost() + 0.20

class Whip(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self) -> str:
        return self.beverage.get_description() + ", Whip"

    def cost(self) -> float:
        return self.beverage.cost() + 0.30
