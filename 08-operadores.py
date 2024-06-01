# operadores

numero_1 = 10
numero_2 = 5

string_1 = "Texto1"
string_2 = "Texto2"

lista_1 = ["valor1", "valor2", "valor3"]
lista_2 = ["valor4", "valor5", "valor6"]

tupla_1 = ("valor1", "valor2", "valor3")
tupla_2 = ("valor4", "valor5", "valor6")

diccionario_1 = {
    "clave1": "valor1",
    "clave2": "valor2",
    "clave3": "valor3"
}

diccionario_2 = {
    "clave4": "valor4",
    "clave5": "valor5",
    "clave6": "valor6"
}

# Operadores aritméticos
# 1. Suma
print(numero_1 + numero_2) # 15
print(string_1 + string_2) # Texto1Texto2
print(lista_1 + lista_2) # ['valor1', 'valor2', 'valor3', 'valor4', 'valor5', 'valor6']
print(tupla_1 + tupla_2) # ('valor1', 'valor2', 'valor3', 'valor4', 'valor5', 'valor6')
# print(diccionario_1 + diccionario_2) # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

# 2. Resta
print(numero_1 - numero_2) # 5
# print(string_1 - string_2) # TypeError: unsupported operand type(s) for -: 'str' and 'str'
# print(lista_1 - lista_2) # TypeError: unsupported operand type(s) for -: 'list' and 'list'
# print(tupla_1 - tupla_2) # TypeError: unsupported operand type(s) for -: 'tuple' and 'tuple'
# print(diccionario_1 - diccionario_2) # TypeError: unsupported operand type(s) for -: 'dict' and 'dict'

# 3. Multiplicación
print(numero_1 * numero_2) # 50
print(string_1 * numero_2) # Texto1Texto1Texto1Texto1Texto1
print(lista_1 * numero_2) # [' 

# 4. División
print(numero_1 / numero_2) # 2.0
# print(string_1 / string_2) # TypeError: unsupported operand type(s) for /: 'str' and 'str'
# print(lista_1 / lista_2) # TypeError: unsupported operand type(s) for /: 'list' and 'list'
# print(tupla_1 / tupla_2) # TypeError: unsupported operand type(s) for /: 'tuple' and 'tuple'
# print(diccionario_1 / diccionario_2) # TypeError: unsupported operand type(s) for /: 'dict' and 'dict'

# 5. Módulo
print(numero_1 % numero_2) # 0
# print(string_1 % string_2) # TypeError: not all arguments converted during string formatting
# print(lista_1 % lista_2) # TypeError: unsupported operand type(s) for %: 'list' and 'list'
# print(tupla_1 % tupla_2) # TypeError: not all arguments converted during string formatting
# print(diccionario_1 % diccionario_2) # TypeError: unsupported operand type(s) for %: 'dict' and 'dict'

# 6. Potencia
print(numero_1 ** numero_2) # 100000
# print(string_1 ** string_2) # TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'str'
# print(lista_1 ** lista_2) # TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'list'
# print(tupla_1 ** tupla_2) # TypeError: unsupported operand type(s) for ** or pow(): 'tuple' and 'tuple'
# print(diccionario_1 ** diccionario_2) # TypeError: unsupported operand type(s) for ** or pow(): 'dict' and 'dict'

# Operadores de comparación
# 7. Igualdad
print(numero_1 == numero_2) # False
print(string_1 == string_2) # False
print(lista_1 == lista_2) # False
print(tupla_1 == tupla_2) # False
print(diccionario_1 == diccionario_2) # False

# 8. Diferencia
print(numero_1 != numero_2) # True
print(string_1 != string_2) # True
print(lista_1 != lista_2) # True
print(tupla_1 != tupla_2) # True
print(diccionario_1 != diccionario_2) # True

# 9. Mayor que
print(numero_1 > numero_2) # True
# print(string_1 > string_2) # TypeError: '>' not supported between instances of 'str' and 'str'
# print(lista_1 > lista_2) # TypeError: '>' not supported between instances of 'list' and 'list'
# print(tupla_1 > tupla_2) # TypeError: '>' not supported between instances of 'tuple' and 'tuple'
# print(diccionario_1 > diccionario_2) # TypeError: '>' not supported between instances of 'dict' and 'dict'

# 10. Menor que
print(numero_1 < numero_2) # False
# print(string_1 < string_2) # TypeError: '<' not supported between instances of 'str' and 'str'
# print(lista_1 < lista_2) # TypeError: '<' not supported between instances of 'list' and 'list'
# print(tupla_1 < tupla_2) # TypeError: '<' not supported between instances of 'tuple' and 'tuple'
# print(diccionario_1 < diccionario_2) # TypeError: '<' not supported between instances of 'dict' and 'dict'

# 11. Mayor o igual que
print(numero_1 >= numero_2) # True
# print(string_1 >= string_2) # TypeError: '>=' not supported between instances of 'str' and 'str'
# print(lista_1 >= lista_2) # TypeError: '>=' not supported between instances of 'list' and 'list'
# print(tupla_1 >= tupla_2) # TypeError: '>=' not supported between instances of 'tuple' and 'tuple'
# print(diccionario_1 >= diccionario_2) # TypeError: '>=' not supported between instances of 'dict' and 'dict'

# 12. Menor o igual que
print(numero_1 <= numero_2) # False
# print(string_1 <= string_2) # TypeError: '<=' not supported between instances of 'str' and 'str'
# print(lista_1 <= lista_2) # TypeError: '<=' not supported between instances of 'list' and 'list'
# print(tupla_1 <= tupla_2) # TypeError: '<=' not supported between instances of 'tuple' and 'tuple'
# print(diccionario_1 <= diccionario_2) # TypeError: '<=' not supported between instances of 'dict' and 'dict'

# Operadores lógicos
# 13. and
print(numero_1 > numero_2 and numero_1 < numero_2) # False
# print(string_1 and string_2) # Texto2 
# print(lista_1 and lista_2) # ['valor4', 'valor5', 'valor6']
# print(tupla_1 and tupla_2) # ('valor4', 'valor5', 'valor6')
# print(diccionario_1 and diccionario_2) # {'clave4': 'valor4', 'clave5': 'valor5', 'clave6': 'valor6'}

# 14. or
print(numero_1 > numero_2 or numero_1 < numero_2) # True
# print(string_1 or string_2) # Texto1
# print(lista_1 or lista_2) # ['valor1', 'valor2', 'valor3']
# print(tupla_1 or tupla_2) # ('valor1', 'valor2', 'valor3')
# print(diccionario_1 or diccionario_2) # {'clave1': 'valor1', 'clave2': 'valor2', 'clave3': 'valor3'}

# 15. not
print(not numero_1 > numero_2) # False
# print(not string_1) # False
# print(not lista_1) # False
# print(not tupla_1) # False
# print(not diccionario_1) # False

# Operadores de identidad
# 16. is
print(numero_1 is numero_2) # False
print(string_1 is string_2) # False
print(lista_1 is lista_2) # False
print(tupla_1 is tupla_2) # False
print(diccionario_1 is diccionario_2) # False

# Operadores de asignación

# 17. Asignación

# 18. Suma y asignación
numero_1 += numero_2
print(numero_1) # 15

# 19. Resta y asignación
numero_1 -= numero_2
print(numero_1) # 10

# 20. Multiplicación y asignación
numero_1 *= numero_2
print(numero_1) # 50

# 21. División y asignación
numero_1 /= numero_2
print(numero_1) # 10.0

# 22. Módulo y asignación
numero_1 %= numero_2
print(numero_1) # 0.0

# Operadores de pertenencia
# 23. in
print(numero_1 in lista_1) # False
print(string_1 in lista_1) # False
print(lista_1 in lista_1) # True
print(tupla_1 in lista_1) # False
print(diccionario_1 in lista_1) # False

# 24. not in
print(numero_1 not in lista_1) # True
print(string_1 not in lista_1) # True
print(lista_1 not in lista_1) # False
print(tupla_1 not in lista_1) # True
print(diccionario_1 not in lista_1) # True

# Operadores logicos
# 25. and
print(True and False) # False
print(True and True) # True
print(False and False) # False
print(False and True) # False
print(numero_1 > numero_2 and "valor1" in lista_1) # False


# 26. or
print(True or False) # True
print(True or True) # True
print(False or False) # False
print(False or True) # True
print(numero_1 < numero_2 or "valor1" in lista_1) # True

# 27. not
print(not True) # False
print(not False) # True
print(not numero_1 > numero_2) # True
print(not "valor1" in lista_1) # False
print(not numero_1 < numero_2 or "valor1" in lista_1) # False

# Operadores de identidad
# 28. is
print(type(numero_1) is int) # True
print(type(string_1) is str) # True
print(type(lista_1) is list) # True
print(type(tupla_1) is tuple) # True
print(type(diccionario_1) is dict) # True

# 29. is not
print(type(numero_1) is not int) # False
print(type(string_1) is not str) # False
print(type(lista_1) is not list) # False
print(type(tupla_1) is not tuple) # False
print(type(diccionario_1) is not dict) # False
