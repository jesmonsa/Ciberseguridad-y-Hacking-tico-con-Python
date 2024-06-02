class Coche:
    
    def __init__(self, velocidad):
        self.atributo_clase = velocidad

    def velocidad_maxima(self):
        print("La velocidad máxima es:", self.atributo_clase)

coche1 = Coche(150)
coche1.velocidad_maxima()

coche2 = Coche(200)
coche2.velocidad_maxima()
