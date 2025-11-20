def generate_board():
    """Generating board"""
    return  [1, 2, 3, 4,
             5, 6, 7, 8,
             9, 10, 11, 12,
             13, 14, 15, 0]


def print_board(board):
    """Function return string-board to print"""
    # TODO
    lines = []
    for i in range(0, 16, 4):
        row = board[i:i+4]
        row_str = " ".join(f"{x if x != 0 else '_':>2}" for x in row)
        lines.append(row_str)
    return "\n".join(lines)


def try_to_move(board, choise):
    """Function check is _choise_-int is possible to change
    position with 0-int in the bord. If movement is possible do it.
    """
    # TODO
    b = board[:]
    try:
        pos_num = b.index(choise)
        pos_zero = b.index(0)
    except ValueError:
        return board

    r_num, c_num = divmod(pos_num, 4)
    r_zero, c_zero = divmod(pos_zero, 4)

    if abs(r_num - r_zero) + abs(c_num - c_zero) == 1:
        b[pos_num], b[pos_zero] = b[pos_zero], b[pos_num]
    return b

def is_board_completed(board):
    """Function return True if the numbers in the board are ordered
    with zero at the finish, otherwise False"""
    # TODO
    return board == [1, 2, 3, 4,
                     5, 6, 7, 8,
                     9, 10, 11, 12,
                     13, 14, 15, 0]


if __name__ == "__main__":
    assert print_board(
        [15,14,13,12,11,10,9,8,7,6,5,4,3,1,0,2]) == "15 14 13 12\n11 10  9  8\n 7  6  5  4\n 3  1  _  2"
    assert try_to_move([15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 1, 2, 0], 2) == [15, 14, 13, 12, 11, 10, 9, 8, 7,
                                                                                      6, 5, 4, 3, 1, 0, 2]
    assert is_board_completed([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]) == True


def play_game():
    import random

    board = generate_board()
    random.shuffle(board)

    while not is_board_completed(board):
        print("\n Try win:")
        print(print_board(board))

        try:
            move = input("Enter your choice : ")

            if move.lower() == 'q':
                print("Exit")
                return

            move = int(move)

            new_board = try_to_move(board, move)
            if new_board == board:
                print("Stop try another choice!")
            else:
                board = new_board

        except ValueError:
            print("Enter number")

    print("\nCongratulation you win!")
    print(print_board(board))


if __name__ == "__main__":
    play_game()

















