
def game_status(board):
    for i in range(3):
        sum = 0
        for j in range(3):
            sum += board[i][j]
        if sum == 3:
            return 1
        elif sum == -3:
            return -1
        
    for j in range(3):
        sum = 0
        for i in range(3):
            sum += board[i][j]
        if sum == 3:
            return 1
        elif sum == -3:
            return -1
            
    sum = board[0][0] + board[1][1] + board[2][2]
    if sum == 3:
        return 1
    elif sum == -3:
        return -1

    sum = board[0][2] + board[1][1] + board[2][0]
    if sum == 3:
        return 1
    elif sum == -3:
        return -1

    return 0
    

def assign_V_train_values(bot1_boards, bot2_boards):
    bot1_train_values = []
    gs = game_status(bot1_boards[len(bot1_boards) - 1])
    for b in bot1_boards:
        bot1_train_values.append([b, gs * 100])    

    bot2_train_values = []
    gs = game_status(bot2_boards[len(bot2_boards) - 1])
    for b in bot2_boards:
        bot2_train_values.append([b, gs * -100])

    return [bot1_train_values, bot2_train_values]




        
    