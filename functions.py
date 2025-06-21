import random

def menu():
    print("1. Atrapar Pokémon")
    print("2. Ver mochila")
    print("3. Desafiar al Gimnasio")
    print("4. Salir del juego")

def opcion():
    try:
        opcion = int(input("Por favor, ingrese la opción del menú a la que desea acceder:\n"))
        return opcion
    except ValueError:
        print("Intentalo nuevamente.")

def welcome():
    print("Bienvenido maestro Pokemón!\n")
    
def pokemon_random(pokemon_salvajes):
    pokemon_aleatorio = random.choice(pokemon_salvajes)
    print(f"Tu pokemon random fue: {pokemon_aleatorio}")
    return pokemon_aleatorio

def quedarse_or_not(mochila, pokemon_aleatorio):
    while True:
        atrapar = input("¿Deseas quedarte con el Pokemón? (S/N)\n").lower()
        
        if atrapar == "s" and len(mochila) <= 6:
            mochila.append(pokemon_aleatorio)
            print("Pokemón agregado exitosamente a tu mochila!")
            print(mochila)
            break

        elif len(mochila) >= 6:
            maximo_pokemon()
            
        elif atrapar == "n":
            print("El Pokemón no fue ingresado a tu lista.")
            break
            
        else:
            print("Favor, intentalo nuevamente")
            continue

def opcion_dos(mochila):     
    if len(mochila) > 0:
        print(f"Tu lista de pokemones es: {mochila}")
    
    else:
        print("aún no has ingresado pokemones ")
        
def opcion_tres(mochila):
    if len(mochila) == 0:
        print("No tienes Pokémon para combatir. ¡Ve a atraparlos primero!")
    
    
    elif len(mochila) > 0:
        batallar(mochila)
    
def batallar(mochila):
    if len(mochila) > 0:
        print(f"Tu lista de pokemones es: {mochila}. Selecciona uno para batallar. Escribe el nombre:\n")
        pokemon_batalla = input("").strip().lower()
        
        if pokemon_batalla == "pikachu":
            print("Ganaste")
        
        elif pokemon_batalla == "charmander":
            print("Perdiste")
        
        elif pokemon_batalla == "bulbasur":
            print("Empataste")
        
        elif pokemon_batalla == "squirtle":
            print("ganaste")
        
        elif pokemon_batalla == "pidgey":
            print("perdiste")
        
        else:
            print("opción no valida")

    else:
        print("aún no has ingresado pokemones ")
      
        
def maximo_pokemon():
    print("Lo sentimos, has alcanzado el máximo de pokemones en tu mochila.")
