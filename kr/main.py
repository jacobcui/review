
from calculator import Calculator

area_triangle = Calculator.Triangle().area(5, 6)
print("Area of triangle is {}".format(area_triangle, ':.2'))

area_square = Calculator.Square().area(5)
print("Area of square is {}".format(area_square, ':.2'))