
try:
    print(var)
except:
    print("La variable no se ha definido previamente")

print("El programa sigue ejecutandose")


try:
    print(var)

except(NameError, ZeroDivisionError):
    print("La variable no se ha definido previamente")

print("El programa sigue ejecutandose")

colores = ('azul', 'verde', 'amarillo')

c = "morado"

if c not in colores:
    raise Exception(f"El color {c} no se encuentra entre los permitidos.")
