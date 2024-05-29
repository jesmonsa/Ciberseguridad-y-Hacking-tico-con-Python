# Listas

# Las listas son un tipo de dato que permite almacenar varios valores en una sola variable.
# Las listas se pueden crear con corchetes [] y los elementos se separan con comas.
# Las listas pueden contener cualquier tipo de dato, incluso otras listas.

# Crear una lista vacía
lista_vacia = []

# Crear una lista con elementos
numeros = [1, 2, 3, 4, 5]
nombres = ['Juan', 'Ana', 'Luis', 'María']
mezcla = [1, 'Juan', 2, 'Ana', 3, 'Luis']

# Lista en una lista (lista anidada) 
lista_anidada = [[1, 2, 3], ['Juan', 'Ana', 'Luis']]
print(lista_anidada)  # [[1, 2, 3], ['Juan', 'Ana', 'Luis']]
print(lista_anidada[0])  # [1, 2, 3]
print(lista_anidada[1])  # ['Juan', 'Ana', 'Luis']

# Acceder a los elementos de una lista
# Los elementos de una lista se pueden acceder mediante un índice.
# Los índices en Python comienzan en 0.
# Para acceder a un elemento se utiliza el nombre de la lista seguido de corchetes [] con el índice del elemento.
# Ejemplo: lista[indice]
print(nombres)  # ['Juan', 'Ana', 'Luis', 'María']
print(numeros)  # [1, 2, 3, 4, 5]
print(mezcla)  # [1, 'Juan', 2, 'Ana', 3, 'Luis']
print(type(nombres))  # <class 'list'>
print(numeros[0])  # 1
print(nombres[1])  # Ana
print(mezcla[2])  # 2
