from abc import ABC, abstractmethod


class AreaCalculator:
    @abstractmethod
    def area(self, *params):
        pass