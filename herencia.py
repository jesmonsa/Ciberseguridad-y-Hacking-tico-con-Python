class Coche():
    """Esta clase representa un coche."""

    def __init__(self, modelo, potencia, consumo):
        """Inicializa los atributos de instancia.

        Argumentos posicionales:
        modelo -- string que representa el modelo del coche
        potencia -- int que representa la potencia en cv
        consumo -- int que representa el consumo en litros/100km
        """
        self.modelo = modelo
        self.potencia = potencia
        self.consumo = consumo
        self.km_actuales = 0

    def especificaciones(self):
        """Muestra las especificaciones del coche."""
        print("Modelo:", self.modelo,
              f"\nPotencia: {self.potencia} cv",
              f"\nConsumo: {self.consumo} l/100km",
              "\nKilometros actuales:", self.km_actuales)

coche = Coche("Seat Ibiza", 90, 5)
coche.especificaciones()
coche1 = Coche("Mercedes Clase A", 150, 7)
coche1.especificaciones()
coche2 = Coche("Audi A3", 120, 6)
coche2.especificaciones()
