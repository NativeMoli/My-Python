def generate_board():
    """Generating board"""
    return []


def print_board(board):
    """Function return string-board to print"""
    # TODO
    return "15 14 13 12\n11 10  9  8\n 7  6  5  4\n 3  1  2  _"


def try_to_move(board, choise):
    """Function check is _choise_-int is possible to change
    position with 0-int in the bord. If movement is possible do it.
    """
    # TODO
    return bord


def is_board_completed(board):
    """Function return True if the numbers in the board are ordered
    with zero at the finish, otherwise False"""
    # TODO
    return False


if __name__ == "__main__":
    assert print_board(
        [15,14,13,12,11,10,9,8,7,6,5,4,3,1,0,2]) == "15 14 13 12\n11 10  9  8\n 7  6  5  4\n 3  1  _  2"
    assert try_to_move([15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 1, 2, 0], 2) == [15, 14, 13, 12, 11, 10, 9, 8, 7,
                                                                                      6, 5, 4, 3, 1, 0, 2]
    assert is_board_completed([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]) == True





















