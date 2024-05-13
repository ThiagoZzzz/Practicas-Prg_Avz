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

# Modelando UMl: ProfesorAyudante --> Profesor --> PersonalUniversitario
#                                '--> Alumno   --> PersonalUniversitario

class PersonalUniversitario():
    def __init__(self, nombre, universidad):
        self.__universidad = universidad
        self.__nombre = nombre

    def get_universidad(self):
        return self.__universidad
    def get_nombre(self):
        return self.__nombre

class Profesor(PersonalUniversitario):
    def __init__(self, nombre, universidad, catedra, comision):
        super().__init__(nombre, universidad)
        self.catedra = catedra
        self.comision = comision
    
    def datos_profesor(self):
        print(f"""
Nombre: {self.get_nombre()}.
Universidad: {self.get_universidad()}. 
Cátedra: {self.catedra}.
Comisión: {self.comision}.
""")

class Alumno(PersonalUniversitario):
    def __init__(self, nombre, universidad, carrera):
        super().__init__(nombre, universidad)
        self.carrera = carrera
        self.cursando = []
    
    def agregar_cursada(self, x):
        self.cursando.append(x)
    
    def datos_alumno(self):
            print(f"""
Nombre: {self.get_nombre()}.
Universidad: {self.get_universidad()}.
Carrera: {self.carrera}.
Materias cursando actualmente: {self.cursando}.
""")

# Ejemplos de uso
# personal_universitario = PersonalUniversitario("John Doe", "University of Examples")
# print(personal_universitario.get_universidad())  
# print(personal_universitario.get_nombre())

# profesor = Profesor("Joe", "University of Examples", "Mathematics", 3)
# profesor.datos_profesor()

# alumno = Alumno("Jane Doe", "University of Examples", "Computer Science")
# alumno.agregar_cursada("Algebra")
# alumno.agregar_cursada("Calculus")
# alumno.datos_alumno()