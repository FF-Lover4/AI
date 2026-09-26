def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(board, player):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    return any(
        board[a] == board[b] == board[c] == player
        for a, b, c in winning_combinations
    )


def tic_tac_toe():
    board = [" "] * 9
    current_player = "X"

    print("TIC-TAC-TOE")
    print("Positions are numbered 1 to 9:")
    print_board([str(i) for i in range(1, 10)])

    for turn in range(9):
        print(f"Player {current_player}'s turn.")

        while True:
            try:
                position = int(input("Choose a position (1-9): "))

                if position < 1 or position > 9:
                    print("Please enter a number from 1 to 9.")
                elif board[position - 1] != " ":
                    print("That position is already taken.")
                else:
                    board[position - 1] = current_player
                    break

            except ValueError:
                print("Please enter a valid number.")

        print_board(board)

        if check_winner(board, current_player):
            print(f"🎉 Player {current_player} wins!")
            return

        current_player = "O" if current_player == "X" else "X"

    print("It's a draw!")


tic_tac_toe()
