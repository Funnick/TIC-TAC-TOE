import random

import TIC_TAC_TOE
import bot

import v_1

import performance_system
import critic
import generalizer

initial_weights = [[random.randint(-10, 10)] * 7, [random.randint(-10, 10)] * 7]
alpha = 1

fd = open('weights.txt', 'a')

for i in range(500):
    if i % 100 == 0:
        alpha /= 10
    boards = performance_system.create_game_history(TIC_TAC_TOE.TIC_TAC_TOE_game(), bot.MixedBot(1, v_1.approximate_board_value, initial_weights[0]), bot.MixedBot(-1, v_1.approximate_board_value, initial_weights[1]))
    V_train_values = critic.assign_V_train_values(boards[0], boards[1])
    initial_weights = generalizer.assing_board_approximation(initial_weights[0], initial_weights[1], v_1.approximate_board_value, V_train_values[0], V_train_values[1], alpha)
    
    
for w in initial_weights:
    for wi in w:
        fd.write(str(wi) + ",")
    fd.write('\n')
fd.write("--------------------\n")
fd.close()
