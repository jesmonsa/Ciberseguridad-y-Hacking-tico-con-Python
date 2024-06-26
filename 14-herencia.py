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

    def actualizar_kilometros(self, kilometros):
        """Actualiza los kilómetros actuales del coche.

        Argumentos posicionales:
        km -- int que representa los kilómetros recorridos
        """
        if kilometros > self.km_actuales:
            self.km_actuales = kilometros 
        else:
            print("No se puede retroceder en el cuentakilómetros.")

coche = Coche("Seat Ibiza", 90, 5)
coche.especificaciones()
coche1 = Coche("Mercedes Clase A", 150, 7)
coche1.especificaciones()
coche2 = Coche("Audi A3", 120, 6)
coche2.especificaciones()

# Asignamos valores a los atributos de instancia

coche1.actualizar_kilometros(2000)

coche1.especificaciones()

print(dir(coche1))

lista = [1, 2, 3, 4, 5]
print(dir(lista))
print(lista)

lista.reverse()
print(lista)

dic = {"a": 1, "b": 2, "c": 3}
print(dic)
print(dir(dic))
print(dic.keys())
print(dic.values())
print(dic.items())

for clave, valor in dic.items():
    print(clave, valor)


dic.pop("a")
print(dic)

# Herencia
class CocheElectrico(Coche):  # Asumiendo que Coche es la clase padre
    def __init__(self, modelo, potencia, consumo, autonomia):
        super().__init__(modelo, potencia, consumo)
        self.autonomia = autonomia

    def especificaciones(self):
        """Muestra las especificaciones del coche eléctrico."""
        print("Modelo:", self.modelo,
              f"\nPotencia: {self.potencia} cv",
              f"\nConsumo: {self.consumo} kWh/100km",
              f"\nAutonomía: {self.autonomia} km")

coche_electrico = CocheElectrico("Tesla Model S", 500, 0, 500)
coche_electrico.especificaciones()


