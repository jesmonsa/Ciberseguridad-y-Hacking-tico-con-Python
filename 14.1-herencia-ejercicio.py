# Clase Dispositivo
class Dispositivo:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.interfaces = []

    def añadir_interfaz(self, interfaz):
        self.interfaces.append(interfaz)

    def mostrar_info(self):
        print(f"Dispositivo: {self.nombre}, Ubicación: {self.ubicacion}")
        for interfaz in self.interfaces:
            print(f"  - Interfaz: {interfaz.nombre}, IP: {interfaz.ip}")

# Clase Interfaz
class Interfaz:
    def __init__(self, nombre, ip):
        self.nombre = nombre
        self.ip = ip

# Clases derivadas Router y Switch
class Router(Dispositivo):
    def __init__(self, nombre, ubicacion, modelo):
        super().__init__(nombre, ubicacion)
        self.modelo = modelo

class Switch(Dispositivo):
    def __init__(self, nombre, ubicacion, tipo):
        super().__init__(nombre, ubicacion)
        self.tipo = tipo

# Ejecución del programa
# Creación del objeto Router
router1 = Router("Router1", "Data Center", "Cisco 2901")
router1.añadir_interfaz(Interfaz("GigabitEthernet0/0", "192.168.1.1"))
router1.añadir_interfaz(Interfaz("GigabitEthernet0/1", "192.168.2.1"))

# Creación del objeto Switch
switch1 = Switch("Switch1", "Oficina Principal", "Capa 3")
switch1.añadir_interfaz(Interfaz("FastEthernet0/0", "192.168.1.2"))
switch1.añadir_interfaz(Interfaz("FastEthernet0/1", "192.168.1.3"))

# Mostrar información de los dispositivos
router1.mostrar_info()
switch1.mostrar_info()
