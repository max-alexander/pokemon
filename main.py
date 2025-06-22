import os, time
from functions import *
import random
from menuselectors import *

pokemon_salvajes = ["Pikachu", "Charmander", "Squirtle", "Bulbasaur", "Pidgey"]
mochila = []
challenged = False

print("🎯 Desafío Pokémon: ¡Conviértete en Maestro Pokémon!\n")

while True:
    
    menu()
    opcion_seleccionada = opcion()
    
    if opcion_seleccionada == option_one:
        pokemon = pokemon_random(pokemon_salvajes)
        quedarse_or_not(mochila, pokemon)
    
    elif opcion_seleccionada == option_two:
        opcion_dos(mochila)
        
    elif opcion_seleccionada == option_three: 
        if challenged == False:
            challenged = opcion_tres(mochila)
        else:
            print("Ya desafiaste al gimnasio. No puedes hacerlo nuevamente.")

    
    elif opcion_seleccionada == option_four:
        print("¡Gracias por jugar, Entrenador/a! ¡Vuelve pronto!")
        break

    else:
        print("Por favor, ingresa una opción válida dentro del menú.")
        