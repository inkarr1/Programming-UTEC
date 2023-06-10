## Requerimientos del Proyecto
Para empezar se debe permitir al usuario seleccionar una opción en el menú principal que va a permitir registrar los jugadores,
establecer los turnos e iniciar el juego de memoria:

- Implementar un menú con 3 opciones:
  1. Registro de jugador con nombre de usuario y contraseña
  2. Establecer turno e iniciar tablero
  3. Iniciar Juego de Memoria

### 1. Registro de jugador con nombre de usuario y contraseña
- Su programa debe implementar el registro del juegador según se indica a continuación:
  - Se solita el nombre de usuario y contraseña
  - Se almacena el usuario y contraseña en variables para usarlo en las siguientes opciones del menú
  - El programa permite crear múltiples jugadores.
  - Opcional: Permite encriptar la contraseña en el programa.
### 2. Establecer el turno e iniciar tablero
- Se solicita la dificultad del tablero entre las siguiente opciones:
  - Fácil: 4 filas y 4 columnas
  - Normal: 4 filas y 8 columnas
  - Dificil: 4 filas y 13 columnas
  Una vez seleccionado el tamaño se debe crear el tablero de juego de la siguiente
  manera seleccionando cartas diferentes y ubicandola en dos posiciones distintas
  - Fácil: Usar 8 cartas distintas
  - Normal: Usar 16 cartas distintas
  - Difícil: Usar 26 cartas distintas
- Se solicita la cantidad de jugadores en un rando de 2 a 4
- Se solicita el usuario y contraseña de los jugadores. Si no es un usuario válido, el programa informa que debe ingresar los datos correctos.
- Si todos los usuarios son validos, se simula sacar una carta aleatoria de la baraja y el orden de juego se realiza con el jugador con la carta hacia la carta menor. En caso hubiera un empate, se vuelven a sacar las cartas.
- Finalmente, se inicializa una matriz con el tamaño de filas y columnas del nivel seleccionado.
### 3. Iniciar Juego de Memoria
- Para la opción de iniciar Juego de Memoria su programa debe realizar lo siguiente:
  - Se valida los jugadores tienen un turno establecido y se les permite empezar el juego. En caso contrario, se le indica que no se ha establecido el turno y que seleccionen la opción 2.
  - Para empezar el juego se muestra el tablero con un número para identificar a cada carta, los números deben ser consecutivos empezando en 1 desde la esquina superior izquierda.
  - Se le permite al jugador seleccionar dos números y se le muestra las cartas seleccionadas.