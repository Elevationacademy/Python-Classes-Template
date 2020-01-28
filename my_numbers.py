class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs


p1 = Polynomial(1, 2, 3)  # x^2 + 2X + 3
p1 = Polynomial(5, 9, 3, 4, 3)  # 5x^4 + 9x^3 + 3x^2 + 4X + 3
