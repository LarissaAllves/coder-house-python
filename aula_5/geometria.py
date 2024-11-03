class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        calcArea = self.base * self.altura
        return calcArea

    def perimetro(self):
        calcPerimetro = 2 * (self.base + self.altura)
        return calcPerimetro
