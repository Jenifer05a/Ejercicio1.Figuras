import math 
class FiguraGeometrica:
    def __init__(self, nombre:str):
        self.nombre=nombre
        
        
class Circulo(FiguraGeometrica):
    def __init__(self, nombre, radio:float):
        super().__init__(nombre)
        self.radio=radio
    
    def calcular_area(self):
        return math.pi * self.radio ** 2
    

class Rectangulo(FiguraGeometrica):
    def __init__(self, nombre, base:float, altura:float):
        super().__init__(nombre)
        self.base=base
        self.altura=altura
        
    def calcular_area(self):
        return self.base * self.altura
        
class Triangulo(FiguraGeometrica):
    def __init__(self, nombre, base:float, altura:float):
        super().__init__(nombre)
        self.base=base
        self.altura=altura
        
    def calcular_area(self):
        return (self.base * self.altura) / 2

   
def main():
    figuras = [
        Circulo("Circulo 1", 6),
        Rectangulo("Rectangulo 1", 7, 4),
        Triangulo("Triangulo 1", 2, 3)
    ]
    
    for figura in figuras:
        print(f"Nombre: {figura.nombre}")
        print(f"Área: {figura.calcular_area():.2f}")
    
if __name__=="__main__":
    main()
        
