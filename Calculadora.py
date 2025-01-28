class Calculadora:
    # TODO: Aplicar encapsulación 
    #       Aplicar estructuras de control

    resultado = 0
    aux = 0
    entrada = 0

    def __init__(self):
        print("Welcome")

    def suma(self):
       self.aux = self.entrada 
       return self.aux
    
    def sumar(self):
       self.aux= self.entrada + self.aux
       return self.aux
    
    def resta(self):
       self.aux= self.entrada 
       return self.aux
    
    def restar(self):
       self.aux= self.entrada - self.aux
       return self.aux
    def multiplica(self):
       self.aux = self.entrada 
       return aux
    def multiplicar(self):
       self.aux = self.entrada * self.aux
       return self.aux
    def divide(self):
       aux = self.entrada 
       return aux
    def dividir(self):
       self.aux = self.aux/self.entrada
       return self.aux
    
    def mostrar_resultado(self):
       self.resultado = self.aux
       return self.resultado
    
    def limpiar(self):
        self.resultado = 0
        self.aux = 0
        self.input = 0
