import math
class Triangle:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
    def is_triangle(self):
        checks = [
        self.a < self.b + self.c,
        self.b < self.c + self.a,
        self.c < self.a + self.b,
        ]
        if all(checks):
            return True
        else:
            return False
    def get_triangle_area(self):
        p = (self.a + self.b + self.c) / 2
        if self.is_triangle():
            return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        else:
            return 0
