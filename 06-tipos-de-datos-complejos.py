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

# Tuplas (tuple) 
# Las tuplas son un tipo de dato similar a las listas, pero son inmutables, es decir, no se pueden modificar.
# Las tuplas se crean con paréntesis () y los elementos se separan con comas.
# Las tuplas pueden contener cualquier tipo de dato, incluso otras tuplas.
# Las tuplas se utilizan para almacenar datos que no deben ser modificados.
# Las tuplas se pueden acceder de la misma forma que las listas.
# Ejemplo: tupla[indice]
tupla_vacia = ()

# Crear una tupla con elementos
numeros = (1, 2, 3, 4, 5)
nombres = ('Juan', 'Ana', 'Luis', 'María')
mezcla = (1, 'Juan', 2, 'Ana', 3, 'Luis')

# Tupla en una tupla (tupla anidada)
tupla_anidada = ((1, 2, 3), ('Juan', 'Ana', 'Luis'))
print(tupla_anidada)  # ((1, 2, 3), ('Juan', 'Ana', 'Luis'))
print(tupla_anidada[0])  # (1, 2, 3)
print(tupla_anidada[1])  # ('Juan', 'Ana', 'Luis')

# Acceder a los elementos de una tupla
print(nombres)  # ('Juan', 'Ana', 'Luis', 'María')
print(numeros)  # (1, 2, 3, 4, 5)
print(mezcla)  # (1, 'Juan', 2, 'Ana', 3, 'Luis')
print(type(nombres))  # <class 'tuple'>
print(numeros[0])  # 1
print(nombres[1])  # Ana
print(mezcla[2])  # 2

# Diccionarios (dict)
# Los diccionarios son un tipo de dato que permite almacenar pares de clave-valor.
# Los diccionarios se crean con llaves {} y los elementos se separan con comas.
# Las claves y los valores se separan con dos puntos :.
# Los diccionarios se utilizan para almacenar datos que se pueden acceder mediante una clave.
# Los diccionarios no tienen un orden definido.
# Los diccionarios se pueden acceder mediante la clave.
# Ejemplo: diccionario[clave]
# Ejemplo: diccionario['nombre']
# Ejemplo: diccionario['edad']
# Ejemplo: diccionario['telefono']
# Ejemplo: diccionario['email']
# Ejemplo: diccionario['direccion']
# Ejemplo: diccionario['ciudad']
# Ejemplo: diccionario['pais']
# Ejemplo: diccionario['codigo_postal']
# Ejemplo: diccionario['fecha_nacimiento']
# Ejemplo: diccionario['altura']
# Ejemplo: diccionario['peso']
# Ejemplo: diccionario['casado']
# Ejemplo: diccionario['hijos']
# Ejemplo: diccionario['mascotas']
# Ejemplo: diccionario['amigos']
# Ejemplo: diccionario['sueldo']
# Ejemplo: diccionario['estudios']
# Ejemplo: diccionario['trabajo']
# Ejemplo: diccionario['empresa']
# Ejemplo: diccionario['cargo']
# Ejemplo: diccionario['jefe']
# Ejemplo: diccionario['subordinados']
# Ejemplo: diccionario['clientes']
# Ejemplo: diccionario['proveedores']
# Ejemplo: diccionario['productos']

# Crear un diccionario vacío
diccionario_vacio = {}

# Crear un diccionario con elementos
persona = {
    'nombre': 'Juan',
    'edad': 30,
    'telefono': '123456789',
    'email': '',
    'direccion': 'Calle 123',
    'ciudad': 'Bogotá',
    'pais': 'Colombia',
    'codigo_postal': '110111',
    'fecha_nacimiento': '01/01/1990',
    'altura': 1.75,
    'peso': 70,
    'casado': False,
    'hijos': 0,
    'mascotas': ['Perro', 'Gato'],
    'amigos': ['Ana', 'Luis'],
    'sueldo': 1000000,
    'estudios': ['Primaria', 'Secundaria', 'Universidad'],
    'trabajo': 'Programador',
    'empresa': 'Empresa S.A.S.',
    'cargo': 'Analista de Sistemas',
    'jefe': 'Pedro',
    'subordinados': ['Maria', 'Carlos'],
    'clientes': ['Empresa A', 'Empresa B'],
    'proveedores': ['Proveedor A', 'Proveedor B'],
    'productos': ['Producto A', 'Producto B']
}

# Acceder a los elementos de un diccionario
print(persona)  # {'nombre': 'Juan', 'edad': 30, 'telefono': '123456789', 'email': '', 'direccion': 'Calle 123', 'ciudad':  
print(type(persona))  # <class 'dict'>
print(persona['nombre'])  # Juan
print(persona['edad'])  # 30
print(persona['telefono'])  # 123456789
print(persona['email'])  # ''
print(persona['direccion'])  # Calle 123
print(persona['ciudad'])  # Bogotá
print(persona['pais'])  # Colombia
print(persona['codigo_postal'])  # 110111
print(persona['fecha_nacimiento'])  # 01/01/1990
print(persona['altura'])  # 1.75
print(persona['peso'])  # 70
print(persona['casado'])  # False
print(persona['hijos'])  # 0
print(persona['mascotas'])  # ['Perro', 'Gato']
print(persona['amigos'])  # ['Ana', 'Luis']
print(persona['sueldo'])  # 1000000
print(persona['estudios'])  # ['Primaria', 'Secundaria', 'Universidad']
print(persona['trabajo'])  # Programador
print(persona['empresa'])  # Empresa S.A.S.
print(persona['cargo'])  # Analista de Sistemas
print(persona['jefe'])  # Pedro
print(persona['subordinados'])  # ['Maria', 'Carlos']
print(persona['clientes'])  # ['Empresa A', 'Empresa B']
print(persona['proveedores'])  # ['Proveedor A', 'Proveedor B']
print(persona['productos'])  # ['Producto A', 'Producto B']


