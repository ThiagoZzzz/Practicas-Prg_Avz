#Repaso parcial
from math import pi
class FiguraGeometrica():
    def __init__(self) -> None:
        pass

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado
    
    def perimetro(self):
        return self.lado * 4

    def area(self):
        return self.lado * self.lado
    def __str__(self):
        return (f"""
Lado: {self.lado}
Perimetro: {self.perimetro()}
Area: {self.area()}""")

class Triangulo(FiguraGeometrica):
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def area(self):
        return (self.lado1 * self.lado2) / 2
    
    def __str__(self):
        return (f"""
Lados: {self.lado1}, {self.lado2}, {self.lado3} 
Perimetro: {self.perimetro()}
Area: {self.area()}""")

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio
    
    def perimetro(self):
        return 2 * pi * self.radio

    def area(self):
        return pi * (self.radio ** 2)
    
    def __str__(self):
        return (f"""
Radio: {self.radio} 
Perimetro: {self.perimetro()}
Area: {self.area()}""")

# #Ejemplos de uso.
# cuadrado = Cuadrado(10)
# print(cuadrado)
# triángulo = Triangulo(3,7,9)
# print(triángulo)
# circulo = Circulo(5)
# print(circulo)
