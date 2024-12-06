from models.board import Board


def test_player_x_wins():
    board = Board()
    board.grid = [['X', 'X', 'X'], ['O', ' ', 'O'], [' ', ' ', ' ']]
    assert board.check_winner() == 'X'

def test_player_o_wins():
    board = Board()
    board.grid = [['X', ' ', ' '], ['O', 'O', 'O'], ['X', ' ', ' ']]
    assert board.check_winner() == 'O'

