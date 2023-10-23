class Binario:
#Obtener el valor del numero ingresado y guardarlo en la variable self.valor
    def __init__(self, valor):
        self.valor = valor
#sumar 1 al valor ingresado
    def avanzar(self):
        self.valor += 1
#mostrar el numero obtenido en binario
    def obtener_valor(self):
        return bin(self.valor)

