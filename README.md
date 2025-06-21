# (INSTRUCCIONES DEL EJERCICIO)

Desafío Pokémon: ¡Conviértete en Maestro Pokémon!

Tu objetivo como entrenador es atrapar Pokémon, revisar tu mochila y desafiar al Gimnasio Eléctrico. 

Para lograrlo, deberás tomar decisiones, manejar tus recursos y elegir bien a tu compañero de combate.

Contenidos que se pondrán en práctica:
• Variables y constantes
• if, elif, else
• Bucles while, for
• try/except
• Tipos de variables
• Banderas
• Listas
• Funciones -->

## Enunciado:
Crea un programa con el siguiente menú principal, que se repite hasta que el jugador elija salir:

=== MENÚ PRINCIPAL ===
1. Atrapar Pokémon
2. Ver mochila
3. Desafiar al Gimnasio
4. Salir del juego

Elige una opción: 
________________________________________
1. Atrapar Pokémon
•	Tienes una lista de Pokémon salvajes (["Pikachu", "Charmander", "Squirtle", "Bulbasaur", "Pidgey"]).
•	En cada intento, aparece un Pokémon aleatorio (puedes usar random.choice() si está permitido, o simularlo con índices).
•	Pregunta al usuario si desea atraparlo (s / n).


•	Si elige "s", agrega el Pokémon a su mochila (otra lista).
•	Solo se pueden atrapar máximo 6 Pokémon.


2. Ver mochila
•	Muestra los Pokémon que el jugador ha atrapado.
•	Si no hay Pokémon, muestra un mensaje adecuado.




3. Desafiar al Gimnasio
•	Si el jugador no tiene Pokémon atrapados, mostrar:

No tienes Pokémon para combatir. ¡Ve a atraparlos primero!

•	Si tiene al menos uno:
o	Mostrar la lista numerada de Pokémon que tiene.
o	Pedirle que elija uno para la batalla.


o	Usar una función batallar(pokemon) que:
	Recibe el Pokémon elegido.
	Usa if/elif/else para determinar si gana o pierde, por ejemplo:

Si elige Pikachu => gana
Si elige Charmander => pierde
Si elige Bulbasaur => empate
(puedes inventar reglas simples)
Mostrar el resultado de la batalla.




4. Salir del juego
Despide al jugador con un mensaje personalizado, por ejemplo:
¡Gracias por jugar, Entrenador/a! ¡Vuelve pronto!


### Reglas adicionales:
Usa funciones para organizar tu código: por ejemplo, mostrar_menu(), atrapar_pokemon(), ver_mochila(), desafiar_gimnasio(), etc.

Usa try/except para manejar errores si el usuario elige un número inválido.

Usa una bandera para indicar si el jugador ya ha ganado en el gimnasio, y evitar que lo desafíe otra vez.
________________________________________
#### Extra (Opcional):
Contar cuántos intentos fallidos tuvo (cuántos Pokémon dijo que no quería).
Permitir eliminar un Pokémon de la mochila si está llena. -->
