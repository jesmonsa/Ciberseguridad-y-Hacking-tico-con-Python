# clases

class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enMarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enMarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)


miCoche = Coche("Mazda", "MX5")
miCoche2 = Coche("Seat", "Leon")
miCoche3 = Coche("Renault", "Megane")

miCoche.estado()
miCoche2.estado()
miCoche3.estado()

