import os, time
from functions import *
import random

pokemon_salvajes = ["Pikachu", "Charmander", "Squirtle", "Bulbasaur", "Pidgey"]
mochila = []

welcome()

while True:
    
    menu()
    opcion_seleccionada = opcion()
    
    if opcion_seleccionada == 1:
        
        pokemon = pokemon_random(pokemon_salvajes)
        quedarse_or_not(mochila, pokemon)
        
    elif opcion_seleccionada == 2:
        opcion_dos(mochila)
        
    elif opcion_seleccionada == 3:
        opcion_tres(mochila)
    
    elif opcion_seleccionada == 4:
        print("¡Gracias por jugar, Entrenador/a! ¡Vuelve pronto!")
        break

    else:
        print("Por favor, ingresa una opción válida dentro del menú.")
        