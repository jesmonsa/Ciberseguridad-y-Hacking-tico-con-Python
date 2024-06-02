# Definir la variable global
puntos_globales = 0

# Definir la función `registro_puntos`
def registro_puntos():
    puntos_partida = 100
    
    # Definir la subfunción `bonus_puntos`
    def bonus_puntos():
        nonlocal puntos_partida
        puntos_partida += 10
        print(f"Bonus aplicado: 10. Puntos de partida después del bonus: {puntos_partida}")
    
    # Aplicar el bonus a los puntos de la partida
    bonus_puntos()
    
    # Modificar la variable global `puntos_globales`
    global puntos_globales
    puntos_globales += puntos_partida
    print(f"Puntos de partida: {puntos_partida}, Puntos globales después de la partida: {puntos_globales}")

# Llamar a la función `registro_puntos`
registro_puntos()

# Imprimir el estado final de la variable global
print(f"Estado final - Puntos globales: {puntos_globales}")
