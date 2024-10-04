class Calculadora:
    def __init__(self):
        self.a = 0
        self.b = 0
    
    #Hice un método diferente para cada operación y separé también cada operación en la consola.

    def sumar(self):
        print("Ingrese los números que se sumarán.")
        self.a = float(input("Ingrese el primer operando: ")) #Solicito el primer número e inmediatamente lo transformo en un float()
        self.b = float(input("Ingrese el segundo operando: ")) #Solicito el segundo número e inmediatamente lo transformo en un float()
        print("El resultado de la suma es: ", self.a + self.b) #Dentro del mismo print hago la operación para no hacer otro método que imprima (def imprimirResultado())
        print()

#Basicamente repito el mismo proceso en las siguientes operacioens

    def restar(self):
        print("Ingrese los números que se restarán.")
        self.a = float(input("Ingrese el primer operando: "))
        self.b = float(input("Ingrese el segundo operando: "))
        print("El resultado de la resta es: ", self.a - self.b)
        print()

    def multiplicar(self):
        print("Ingrese los números que se multiplicarán.")
        self.a = float(input("Ingrese el primer operando: "))
        self.b = float(input("Ingrese el segundo operando: "))
        print("El resultado de la multiplicación es: ", self.a * self.b)
        print()

    def dividir(self):
        print("Ingrese los números que se dividirán.")
        self.a = float(input("Ingrese el primer operando: "))
        self.b = float(input("Ingrese el segundo operando: "))
        
        if self.b == 0:
            print("¿Cómo crees que voy a dividir entre 0?")
        else:
            print("El resultado de la división es: ", self.a / self.b)
            print()