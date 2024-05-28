# variables

# Variables are used to store data values.

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
nivel = input("Ingrese su nivel de estudios: ")

print("Hola, mi nombre es " + nombre + ", tengo " + edad + " años y mi nivel de estudios es " + nivel + ".")

# Como nombrar variables en Python

# Una variable puede tener un nombre corto (como x e y) o un nombre más descriptivo (edad, nombre, total_votos).
# Reglas para nombrar variables en Python:
# - Un nombre de variable debe comenzar con una letra o el carácter de subrayado
# - Un nombre de variable no puede comenzar con un número
# - Un nombre de variable solo puede contener caracteres alfanuméricos y guiones bajos (A-z, 0-9 y _)
# - Los nombres de las variables distinguen entre mayúsculas y minúsculas (nombre, Nombre y NOMBRE son tres variables diferentes)

# Ejemplos de nombres de variables válidos
miVariable = "Hola"
mi_variable = "Hola"
_mi_variable = "Hola"
MIVARIABLE = "Hola"
miVariable2 = "Hola"

# Ejemplos de nombres de variables no válidos
# 2miVariable = "Hola"
# mi-Variable = "Hola"
# mi Variable = "Hola"

# Asignar valor a una variable

# Python no requiere declarar explícitamente el tipo de variable, como Java. Python asume automáticamente el tipo de datos de la variable según el valor asignado.

x = 5
y = "Hola"

print(x)
print(y)

# Asignar el mismo valor a múltiples variables

x = y = z = "Naranja"

print(x)
print(y)
print(z)

# Variables de salida

# La función print() se usa para imprimir variables.

x = "Python es "
y = "increíble"

print(x + y)
