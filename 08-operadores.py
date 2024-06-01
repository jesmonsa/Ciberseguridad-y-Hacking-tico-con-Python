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

# Operadores de comparación
# 13. Y


