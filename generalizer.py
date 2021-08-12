def assing_board_approximation(bot1_weights, bot2_weights, V_approx, bot1_V_train_values, bot2_V_train_values, alpha):
    for b_V_train in bot1_V_train_values:
        b_approx_value_and_xi = V_approx(b_V_train[0], bot1_weights)
        b_approx_value = b_approx_value_and_xi[len(b_approx_value_and_xi) - 1]
        for i in range(len(bot1_weights)):
            bot1_weights[i] = bot1_weights[i] + alpha * (b_V_train[1] - b_approx_value) * b_approx_value_and_xi[i]


    for b_V_train in bot2_V_train_values:
        b_approx_value_and_xi = V_approx(b_V_train[0], bot2_weights)
        b_approx_value = b_approx_value_and_xi[len(b_approx_value_and_xi) - 1]
        for i in range(len(bot2_weights)):
            bot2_weights[i] = bot2_weights[i] + alpha * (b_V_train[1] - b_approx_value) * b_approx_value_and_xi[i] 

    
    return [bot1_weights, bot2_weights]
