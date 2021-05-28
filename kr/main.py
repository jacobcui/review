
from calculator import Calculator

area_triangle = Calculator.Triangle().area(5, 3.11)
print("Area of triangle is {:.2f}".format(area_triangle))

area_square = Calculator.Square().area(5)
print("Area of square is {:.2f}".format(area_square))