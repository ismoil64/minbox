from math import pi
from typing import List, Callable

class Figure:
    def __init__(self):
        self.figures = {1: self.circle_square, 3: self.triangle_square}

    def check_nums(self, nums: List[float]):
        if not nums:
            raise ValueError("Необходимо передать данные")
        for n in nums:
            if not isinstance(n, (int, float)) or n <= 0:
                raise ValueError("Некорректные данные")

    def triangle_square(self, a: float, b: float, c: float) -> float:
        sides = [a, b, c]
        sides.sort()
        if sides[0] ** 2 + sides[1] ** 2 != sides[2] ** 2:
            raise ValueError("Некорректные стороны треугольника")
        return (a * b) / 2

    def add_figure(self, quantity: int, formula: Callable):
        self.figures[quantity] = formula

    def circle_square(self, radius: float) -> float:
        return pi * (radius ** 2)     

    def find_square(self, *args: float) -> float:
        self.check_nums(args)
        if len(args) not in self.figures:
            raise ValueError("Не найдена формула для такой фигуры")
        formula = self.figures[len(args)]
        return round(formula(*args), 2)

figure = Figure()
