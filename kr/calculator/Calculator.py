from .Abstract import AreaCalculator


class Square(AreaCalculator):
    # noinspection PyMethodMayBeStatic
    def area(self, *params):
        return float(params[0] ** 2)

class Triangle(AreaCalculator):
    # noinspection PyMethodMayBeStatic
    def area(self, *params):
        """Calculates the area for a triangle.
        
        Args:
          *params: 2 items iterable indicating the height and width.
        Returns:
          Decimal indicating the area value.
        """
        return params[0] * params[1] / 2.0