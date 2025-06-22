import random
import os

def menu():
    print("Menú")
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

def pokemon_random(pokemon_salvajes):
    pokemon_aleatorio = random.choice(pokemon_salvajes)
    print(f"Tu pokemon random fue: {pokemon_aleatorio}")
    return pokemon_aleatorio

def quedarse_or_not(mochila, pokemon_aleatorio):
    while True:
        atrapar = input(f"¿Deseas quedarte con el Pokemón '{pokemon_aleatorio}'? (S/N)\n").lower()

        if len(mochila) == 6:
            print("Atención: Tu mochila está llena")

            ask_delete = input("¿Desea eliminar algún pokemón para liberar espacio? (S/N)").strip().lower()
            if ask_delete == "s":
                for i in range(len(mochila)):
                    print(f"{i + 1} - {mochila[i]}")
            
                pokemon_to_delete = int(input("Ingrese el indice del pokemón que desea eliminar"))
                os.system("cls")

                try:
                    del mochila[pokemon_to_delete - 1]
                    print(f"Pokemón {mochila[pokemon_to_delete -1]} eliminado con éxito")

                except IndexError:
                    print("Indice no válido")
                    break
            
            elif ask_delete == "n":
                os.system("cls")
                break
            
            else:
                print("Opción no válida. Intentelo nuevamente")

        elif atrapar == "s" and 0 <= len(mochila) <= 6:
            mochila.append(pokemon_aleatorio)
            print("Pokemón agregado exitosamente a tu mochila!")
            print(mochila)
            break

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
        return False
    
    
    elif len(mochila) > 0:
        return batallar(mochila)

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
            return False
        
        return True
        
    else:
        print("aún no has ingresado pokemones ")