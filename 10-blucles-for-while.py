# Bucles

# Bucle for
for i in range(5):
    print(i)

lista = ["uno", "dos", "tres", "cuatro", "cinco"]
for i in lista:
    print(i)

for i in range(len(lista)):
    print(lista[i])

for tarea in lista:
    print("Estoy trabajando en la tarea: ", tarea)

lista_tareas = {
    "tarea1": "Hacer la compra",
    "tarea2": "Lavar el coche",
    "tarea3": "Pasear al perro",
    "tarea4": "Estudiar Python",
    "tarea5": "Hacer deporte"
}

for tarea in lista_tareas:
    print("Tarea: ", tarea)
    print("Descripción: ", lista_tareas[tarea])


# Bucle while
i = 0
while i < 5:
    print(i)
    i += 1

num = 0
while num < 10:
    print(num)
    num += 1

while num > 0:
    num -= 1
    print(num)
   