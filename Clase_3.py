#Ejercicio 2.
class Punto():
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
    
    def eje_x(self):
        return self.x
    
    def eje_y(self):
        return self.y
    
    def imprimir(self):
        print(f"({str(self.x)}, {str(self.y)})")
    
    def opuesto(self):
        return (Punto(- self.eje_x(), -self.eje_y()))


#Ejercicio 3.
class Linea():
    def __init__(self, p1, p2):
        if isinstance(p1, Punto) and isinstance(p2, Punto):
            self._punto_a = p1
            self._punto_b = p2
        else:
            raise TypeError("Los argumentos deben ser instancias de la clase Punto.")

    def mueve_derecha (self, n=float):
        return (self._punto_a.x + n, self._punto_a.y), (self._punto_b.x + n, self._punto_b.y)
    def mueve_izquierda (self, n=float):
        return (self._punto_a.x - n, self._punto_a.y), (self._punto_b.x - n, self._punto_b.y)
    
    def mueve_arriba (self, n=float):
        return (self._punto_a.x, self._punto_a.y + n), (self._punto_b.x, self._punto_b.y + n)
    def mueve_abajo (self, n=float):
        return (self._punto_a.x, self._punto_a.y - n), (self._punto_b.x, self._punto_b.y - n)

#Ejercicio 4.
class Cancion():
    def __init__(self, titulo, autor):
        self.titulo = str(titulo)
        self.autor = str(autor)
    
    def get_titulo(self):
        return self.titulo
    def get_autor(self):
        return self.autor
    
    def set_titulo(self, new_titulo = str):
        self.titulo = new_titulo
    def set_autor(self, new_autor = str):
        self.titulo = new_autor
    #método adicional
    def imprimir(self):
        print(f"-{self.titulo}-, by {self.autor}.")

#Ejercicio 5.
from datetime import date
class Persona():
    def __init__(self, nombre, ocupacion, fecha_nacimiento):    #la fecha de nacimiento se recibe con el siguiente formato -> AAAA-MM-DD
        self.nombre = str(nombre)
        self.ocupacion = str(ocupacion)
        self.fecha_nacimiento = fecha_nacimiento
    
    def calcular_edad(self):
        hoy = date.today()
        edad = hoy.year - self.fecha_nacimiento.year - ((hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
        return edad

class Libro():
    def __init__(self, titulo, autor, ISBN, paginas, edicion, editorial, ciudad, pais, fecha_edicion):
        if isinstance(autor, Persona):
            self.titulo = str(titulo)
            self.autor = autor
            self.ISBN = str(ISBN)
            self.paginas = int(paginas)
            self.edicion = str(edicion)
            self.editorial = str(editorial)
            self.lugar = str(ciudad), str(pais)
            self.fecha_edicion = str(fecha_edicion)
        else:
            raise TypeError("El autor debe ser una instancia de la clase Persona.")
    
    def get_titulo(self):
        return self.titulo
    def get_autor(self):
        return self.autor
    def get_ISBN(self):
        return self.ISBN
    def get_paginas(self):
        return self.paginas
    def get_edicion(self):
        return self.edicion
    def get_editorial(self):
        return self.editorial
    def get_lugar(self):
        return self.lugar
    def get_fecha_edicion(self):
        return self.fecha_edicion

    def set_titulo(self, new_titulo):
        self.titulo = new_titulo
    def set_autor(self, new_autor):
        self.autor = new_autor
    def set_ISBN(self, new_ISBN):
        self.ISBN = new_ISBN
    def set_paginas(self, new_paginas):
        self.paginas = new_paginas
    def set_edicion(self, new_edicion):
        self.edicion = new_edicion
    def set_editorial(self, new_editorial):
        self.editorial = new_editorial
    def set_lugar(self, new_ciudad, new_pais):
        self.lugar = new_ciudad, new_pais
    
    def informacion(self):
        print(f"""
            Título: {self.get_titulo()}
            Edición : {self.get_edicion()}
            Editorial: {self.get_editorial()}
            ISBN: {self.get_ISBN()}
            Páginas: {self.get_paginas()}
            Lugar: {self.get_lugar()}
                    """)

p = Persona("Javier","Docente","1979-08-22")
