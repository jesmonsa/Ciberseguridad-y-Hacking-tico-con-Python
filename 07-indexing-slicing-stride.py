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