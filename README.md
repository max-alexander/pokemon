# 🧪 INSTRUCCIONES DEL EJERCICIO

## 🎯 Desafío Pokémon: ¡Conviértete en Maestro Pokémon!

Tu objetivo como entrenador es **atrapar Pokémon**, **revisar tu mochila** y **desafiar al Gimnasio Eléctrico**.  
Para lograrlo, deberás tomar decisiones, administrar tus recursos y elegir sabiamente a tu compañero de combate.

---

### 📚 Contenidos que pondrás en práctica:
- Variables y constantes
- Estructuras de control: `if`, `elif`, `else`
- Bucles: `while`, `for`
- Manejo de errores con `try/except`
- Tipos de variables
- Uso de banderas (flags)
- Listas
- Funciones

---

## 📝 Enunciado

Crea un programa con el siguiente **menú principal**, que se repetirá hasta que el jugador elija salir:


---

### 1️⃣ Atrapar Pokémon
- Tienes una lista de Pokémon salvajes:  
  `["Pikachu", "Charmander", "Squirtle", "Bulbasaur", "Pidgey"]`
- En cada intento, aparece un Pokémon aleatorio.
  - Puedes usar `random.choice()` o simular la aleatoriedad con índices.
- Pregunta al usuario si desea atraparlo (`s` / `n`).
- Si elige "s", agrega el Pokémon a su **mochila** (otra lista).
- Máximo 6 Pokémon pueden estar en la mochila.
- Si está llena, permite eliminar uno para hacer espacio. *(opcional)*

---

### 2️⃣ Ver mochila
- Muestra los Pokémon atrapados por el jugador.
- Si la mochila está vacía, muestra un mensaje adecuado.

---

### 3️⃣ Desafiar al Gimnasio
- Si no hay Pokémon atrapados, muestra:

- Si tiene al menos uno:
- Muestra la lista numerada de Pokémon.
- Solicita al jugador elegir uno para la batalla.
- Llama a la función `batallar(pokemon)` que:
  - Recibe el Pokémon elegido.
  - Usa condiciones (`if/elif/else`) para definir el resultado:

    | Pokémon       | Resultado |
    |---------------|-----------|
    | Pikachu       | Gana      |
    | Charmander    | Pierde    |
    | Bulbasaur     | Empate    |
    | Otros         | Resultado aleatorio o inventado |

  - Muestra el resultado de la batalla.
- Usa una **bandera** para evitar que el gimnasio sea desafiado más de una vez.

---

### 4️⃣ Salir del juego
Despide al jugador con un mensaje personalizado, por ejemplo:  
**¡Gracias por jugar, Entrenador/a! ¡Vuelve pronto!**

---

## 🛠️ Reglas adicionales
- Usa **funciones** para organizar tu código:
- `mostrar_menu()`
- `atrapar_pokemon()`
- `ver_mochila()`
- `desafiar_gimnasio()`
- Usa `try/except` para manejar errores al ingresar opciones inválidas.
- Controla la lógica del juego con una **bandera de victoria**.

---

## ⭐ Extra (Opcional)
- Llevar la cuenta de cuántos intentos fallidos tuvo el jugador (Pokémon rechazados).
- Permitir **eliminar Pokémon** de la mochila si está llena.

---

¡Buena suerte, Entrenador! 🧢⚡
