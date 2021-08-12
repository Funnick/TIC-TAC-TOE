import TIC_TAC_TOE
import bot

def create_game_history(game, bot1, bot2):
    bot1_boards = []
    bot2_boards = []

    while(True):
        move = bot1.play(game.get_valid_moves(), game.get_board())
        game.change_state(1, move)
        gs = game.game_status()
        bot1_boards.append(game.get_board())
        if gs != 2:
            bot2_boards.append(game.get_board())
            break

        move = bot2.play(game.get_valid_moves(), game.get_board())
        game.change_state(-1, move)
        gs = game.game_status()
        bot2_boards.append(game.get_board())
        if gs != 2:
            bot1_boards.append(game.get_board())
            break

    return [bot1_boards, bot2_boards]
