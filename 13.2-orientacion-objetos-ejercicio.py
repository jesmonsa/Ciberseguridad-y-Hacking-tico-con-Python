class Vulnerabilidad:
    def __init__(self, nombre, severidad, descripcion):
        self.nombre = nombre
        self.severidad = severidad
        self.descripcion = descripcion

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}\nSeveridad: {self.severidad}\nDescripción: {self.descripcion}")

    def recomendar_acciones(self):
        if self.severidad == "Crítica":
            recomendacion = "Aplicar parches de seguridad inmediatamente y revisar sistemas afectados."
        elif self.severidad == "Alta":
            recomendacion = "Realizar una auditoría de seguridad y aplicar medidas correctivas lo antes posible."
        elif self.severidad == "Media":
            recomendacion = "Monitorear la actividad del sistema y planificar la aplicación de parches."
        elif self.severidad == "Baja":
            recomendacion = "Mantener bajo observación y revisar en el próximo ciclo de actualización."
        print(f"Acción recomendada: {recomendacion}")

# Crear objetos de la clase Vulnerabilidad
vuln1 = Vulnerabilidad("SQL Injection", "Alta", "Permite la ejecución de consultas SQL no autorizadas.")
vuln2 = Vulnerabilidad("XSS", "Media", "Permite la ejecución de scripts en el navegador del usuario.")
vuln3 = Vulnerabilidad("Desbordamiento de Buffer", "Crítica", "Permite la ejecución arbitraria de código.")

# Crear lista para contener los objetos
registro_vulnerabilidades = [vuln1, vuln2, vuln3]

# Recorrer la lista y mostrar información
for vulnerabilidad in registro_vulnerabilidades:
    vulnerabilidad.mostrar_info()
    vulnerabilidad.recomendar_acciones()
    print()  # Línea en blanco para separar la salida de cada vulnerabilidad
