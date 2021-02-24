from copy import deepcopy
import pygame

RED = (255, 0, 0)
WHITE = (255, 255, 255)


def algorithm(position, depth, max_player, game):
    if depth == 0 or game.winner() is not None:
        return position.evaluate(), position

    if max_player:
        max_eval = float('-inf')
        best_move = None
        for move in get_all_moves(position, WHITE):
            evaluation = algorithm(move, depth - 1, False, game)[0]
            max_eval = max(max_eval, evaluation)
            if max_eval == evaluation:
                best_move = move

        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for move in get_all_moves(position, RED):
            evaluation = algorithm(move, depth - 1, True, game)[0]
            min_eval = min(min_eval, evaluation)
            if min_eval == evaluation:
                best_move = move

        return min_eval, best_move


def simulate_move(piece, move, board, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


def get_all_moves(board, color):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            # draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, skip)
            moves.append(new_board)
    return moves


def get_a_move(board, color):
    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for _ in valid_moves.items():
            return True
    return False


def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0, 255, 0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    # pygame.time.delay(100)
