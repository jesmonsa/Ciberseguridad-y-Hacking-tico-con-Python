# Lista de tareas
# 1. Crear una lista de tareas con 5 tareas

lista_tareas = ["tarea1", "tarea2", "tarea3", "tarea4", "tarea5"]

# Tupla de tareas
# 2. Crear una tupla con 5 tareas

tupla_tareas = ("tarea1", "tarea2", "tarea3", "tarea4", "tarea5")

# Diccionario de tareas
# 3. Crear un diccionario con 5 tareas

diccionario_tareas = {
    "tarea1": "pendiente",
    "tarea2": "en proceso",
    "tarea3": "pendiente",
    "tarea4": "terminada",
    "tarea5": "en proceso"
}

# Indexing
# 4. Imprimir la primera tarea de la lista de tareas

print(lista_tareas[0]) # tarea1
print(lista_tareas[1]) # tarea2
print(lista_tareas[-1]) # tarea5
print(lista_tareas[1][1]) # a
print(lista_tareas[1][-1]) # 2

# 5. Imprimir la segunda tarea de la tupla de tareas

print(tupla_tareas[1]) # tarea2
print(tupla_tareas[2]) # tarea3

# 6. Imprimir el estado de la tercera tarea del diccionario de tareas

print(diccionario_tareas["tarea3"]) # pendiente
print(diccionario_tareas["tarea4"]) # terminada

# Slicing

# 7. Imprimir las primeras 3 tareas de la lista de tareas

print(lista_tareas[0:3]) # ['tarea1', 'tarea2', 'tarea3']
print(lista_tareas[:3]) # ['tarea1', 'tarea2', 'tarea3']
print(lista_tareas[1:4]) # ['tarea2', 'tarea3', 'tarea4']
print(lista_tareas[1:]) # ['tarea2', 'tarea3', 'tarea4', 'tarea5']

# 8. Imprimir las últimas 3 tareas de la tupla de tareas

print(tupla_tareas[-3:]) # ('tarea3', 'tarea4', 'tarea5')
print(tupla_tareas[-2:]) # ('tarea4', 'tarea5')

# 9. Imprimir las tareas pendientes del diccionario de tareas

for tarea, estado in diccionario_tareas.items():
    if estado == "pendiente":
        print(tarea)

# Stride

# 10. Imprimir las tareas de la lista de tareas de dos en dos

print(lista_tareas[::2]) # ['tarea1', 'tarea3', 'tarea5']
print(lista_tareas[1::2]) # ['tarea2', 'tarea4']

# 11. Imprimir las tareas de la tupla de tareas de dos en dos

print(tupla_tareas[::2]) # ('tarea1', 'tarea3', 'tarea5')
print(tupla_tareas[1::2]) # ('tarea2', 'tarea4')

# 12. Imprimir las tareas del diccionario de tareas de dos en dos

for i, (tarea, estado) in enumerate(diccionario_tareas.items()): 
    if i % 2 == 0:
        print(tarea)

# 13. Imprimir las tareas del diccionario de tareas de dos en dos

for i, (tarea, estado) in enumerate(diccionario_tareas.items()):
    if i % 2 != 0:
        print(tarea)

# 14. Imprimir las tareas del diccionario de tareas de dos en dos

for i, (tarea, estado) in enumerate(diccionario_tareas.items()):
    if i % 2 == 0:
        print(estado)

# 15. Imprimir las tareas del diccionario de tareas de dos en dos

for i, (tarea, estado) in enumerate(diccionario_tareas.items()):
    if i % 2 != 0:
        print(estado)

# 16. Imprimir las tareas del diccionario de tareas de dos en dos

for i, (tarea, estado) in enumerate(diccionario_tareas.items()):
    if i % 2 == 0:
        print(tarea, estado)

# 17. Imprimir las tareas del diccionario de tareas de dos en dos

for i, (tarea, estado) in enumerate(diccionario_tareas.items()):
    if i % 2 != 0:
        print(tarea, estado)

# Modificar tareas

# 18. Modificar la primera tarea de la lista de tareas

lista_tareas[0] = "tarea1 modificada"
print(lista_tareas)

# 19. Modificar la segunda tarea de la tupla de tareas

tupla_tareas = list(tupla_tareas)
tupla_tareas[1] = "tarea2 modificada"
tupla_tareas = tuple(tupla_tareas)
print(tupla_tareas)

# 20. Modificar el estado de la tercera tarea del diccionario de tareas

diccionario_tareas["tarea3"] = "terminada en caliente"
print(diccionario_tareas)



