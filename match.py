import TIC_TAC_TOE
import bot
import v_1

game = TIC_TAC_TOE.TIC_TAC_TOE_game()
print("Ser jugador 1 o -1?")
p = int(input())

if p == 1:
    bot_player = bot.VBot(-1, v_1.approximate_board_value, 
    [-25.29801060445754, 4.129576131953858, 2.3142731428915493, -31.706794105620762, 14.332079669984429, -55.263242355831544, 91.75279158519541])
else:
    bot_player = bot.VBot(1, v_1.approximate_board_value, 
    [30.050340826148016, 3.411285479986387, -3.5322074526880414, 4.159594578018466, -43.87888955059849, 59.211023636555204, -96.17732042009645])

game.print_board()
print()
if p == 1:
    while(True):
        i, j = [int(k) for k in input().split()]
        print()
        game.change_state(1, [i, j])
        game.print_board()
        print()
        gs = game.game_status()
        if gs != 2:
            break

        move = bot_player.play(game.get_valid_moves(), game.get_board())
        game.change_state(-1, move)
        game.print_board()
        print()
        gs = game.game_status()
        if gs != 2:
            break
else:
    while(True):
        move = bot_player.play(game.get_valid_moves(), game.get_board())
        game.change_state(1, move)
        game.print_board()
        print()
        gs = game.game_status()
        if gs != 2:
            break

        i, j = [int(k) for k in input().split()]
        print()
        game.change_state(-1, [i, j])
        game.print_board()
        print()
        gs = game.game_status()
        if gs != 2:
            break

        
if gs != 0:
    print('Gana', gs)
else:
    print('Empate')