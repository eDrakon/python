from random import randrange

board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]


def display_board(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    separation_row = "+-------+-------+-------+"
    normal_row = "|       |       |       |"
    for i in range(13):
        if i % 4 == 0:
            print(separation_row)
            continue
        if i == 2:
            print(f"|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |")
            continue
        if i == 6:
            print(f"|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |")
            continue
        if i == 10:
            print(f"|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |")
            continue
        print(normal_row)


def enter_move(board, move=0, player="human"):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    while True:
        try:
            if player == "human":
                move = int(input("Ingresa tu movimiento: "))
                sign = "o"
            else:
                sign = "x"
            move -= 1
            row = move // 3
            col = move % 3
            have_sign = board[row][col]
            if have_sign in ["x", "o"]:
                raise ValueError("La casilla ya está ocupada.")
            board[row][col] = sign
            break
        except Exception as error:
            print(error)    

def victory_for(board):
    #     # La función analiza el estatus del tablero para verificar si
    #     # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    if (
        board[0][0] == board[0][1] == board[0][2] == "o"
        or board[1][0] == board[1][1] == board[1][2] == "o"
        or board[2][0] == board[2][1] == board[2][2] == "o"
        or board[0][0] == board[1][0] == board[2][0] == "o"
        or board[0][1] == board[1][1] == board[2][1] == "o"
        or board[0][2] == board[1][2] == board[2][2] == "o"
        or board[0][0] == board[1][1] == board[2][2] == "o"
        or board[0][2] == board[1][1] == board[2][0] == "o"
    ):
        return "¡Has ganado!"
    if (
        board[0][0] == board[0][1] == board[0][2] == "x"
        or board[1][0] == board[1][1] == board[1][2] == "x"
        or board[2][0] == board[2][1] == board[2][2] == "x"
        or board[0][0] == board[1][0] == board[2][0] == "x"
        or board[0][1] == board[1][1] == board[2][1] == "x"
        or board[0][2] == board[1][2] == board[2][2] == "x"
        or board[0][0] == board[1][1] == board[2][2] == "x"
        or board[0][2] == board[1][1] == board[2][0] == "x"
    ):
        return "Gana la máquina"
    if len(free_fields(board)) == 0:
        return "Empate"


def machine_move(free_fields):
    #     La función dibuja el movimiento de la máquina y actualiza el tablero.
    enter_move(board, free_fields[randrange(0, len(free_fields))], "machine")


def free_fields(board):
    #     # La función examina el tablero y construye una lista de todos los cuadros
    #     # vacíos. La lista esta compuesta por tuplas, cada tupla es un par de números
    #     # que indican la fila y columna.
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ["o", "x"]:
                free_fields.append(board[row][col])
    return free_fields


while True:
    display_board(board)
    enter_move(board)
    machine_move(free_fields(board))
    if victory_for(board) is not None:
        display_board(board)
        print("El ganador es: {0}".format(victory_for(board)))
        another_game = input("¿Deseas jugar otra vez? (s/n): ")
        if another_game == "s":
            board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            continue
        else:
            break
