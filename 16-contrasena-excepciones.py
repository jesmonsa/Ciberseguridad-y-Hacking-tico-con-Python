import re

def validar_contraseña(contraseña):
    if len(contraseña) < 8:
        raise ValueError("La contraseña no cumple con los criterios establecidos: debe tener al menos 8 caracteres de longitud.")
    if not any(char.isupper() for char in contraseña):
        raise ValueError("La contraseña no cumple con los criterios establecidos: debe contener al menos una letra mayúscula.")
    if not any(char.islower() for char in contraseña):
        raise ValueError("La contraseña no cumple con los criterios establecidos: debe contener al menos una letra minúscula.")
    if not any(char.isdigit() for char in contraseña):
        raise ValueError("La contraseña no cumple con los criterios establecidos: debe contener al menos un número.")
    if not any(char in "@#$%^&*()!" for char in contraseña):
        raise ValueError("La contraseña no cumple con los criterios establecidos: debe contener al menos un símbolo especial (@, #, $, %, &, *, etc.).")
    return True

def main():
    contraseña = "contraseña1!"
    print(f"Validando contraseña {contraseña}")
    
    try:
        if validar_contraseña(contraseña):
            print("La contraseña es segura.")
    except ValueError as e:
        print(f"Se ha producido una excepción: {e}")

if __name__ == "__main__":
    main()
