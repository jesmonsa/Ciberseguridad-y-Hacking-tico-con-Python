# Funciones

# Ejemlos de funciones en Python
print("Esto es una cadena de texto")
print(len("Esto es una cadena de texto"))

# Definir una función
def mi_funcion():
    print("Hola desde mi función")

# Llamar a la función
mi_funcion()

# Función con parámetros
def mi_funcion2(arg1, arg2):
    print(arg1 + arg2)

# función con parámetros posicionales

def mi_funcion3(arg1, arg2):
    print(arg1)
    print(arg2)

mi_funcion3(arg2="valor2", arg1="valor1")

# Función con retorno
def mi_funcion4(arg1, arg2):
    return arg1 + arg2

resultado = mi_funcion4(1, 2)
print(resultado)

# Funciones con valores por defecto
def mi_funcion5(arg1, arg2=100):
    return arg1 + arg2

resultado = mi_funcion5(1)
print(resultado)

# Funciones con retorno múltiple
def mi_funcion6(arg1, arg2):
    return arg1 + arg2, arg1 - arg2

resultado = mi_funcion6(10, 5)
print(resultado)



