def approximate_board_value(board, weights):
    board_features = [1] + [0] * 7

    aux = [[0 for i in range(3)] for j in range(8)]

    for i in range(3):
        for j in range(3):
            ind = 2
            if board[i][j] == 1:
                ind = 0
            elif board[i][j] == -1:
                ind = 1
            
            aux[i][ind] += 1
            aux[j + 3][ind] += 1

            if i == j:
                aux[6][ind] += 1
            if (i == 2 and j == 0) or (i == 1 and j == 1) or (i == 0 and j == 2):
                aux[7][ind] += 1

    for i in range(len(aux)):
        if aux[i][2] != 3:
            if aux[i][1] == 0:
                board_features[2 * aux[i][0] - 1] += 1
            if aux[i][0] == 0:
                board_features[2 * aux[i][1]] += 1

    for i in range(7):
        board_features[7] += weights[i] * board_features[i] 

    return board_features