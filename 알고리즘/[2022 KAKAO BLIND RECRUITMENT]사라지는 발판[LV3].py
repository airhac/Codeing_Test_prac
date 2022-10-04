def A_turn(board, a_x, a_y, b_x, b_y, cnt):
    n = len(board)
    m = len(board[0])
    dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
    if board[a_x][a_y] == 0:
        return 1, cnt
    winner = []
    loser = []
    check = False
    for i in range(4):
        nx, ny = a_x + dx[i], a_y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1:
            check = True
            board[a_x][a_y] = 0
            is_win, score = B_turn(board, b_x, b_y, nx, ny, cnt + 1)
            board[a_x][a_y] = 1
            if is_win:
                winner.append(score)
            else:
                loser.append(score)
    if check:
        if winner:
            return 0, min(winner)
        else:
            return 1, max(loser)
    else:
        return 1, cnt
def B_turn(board, b_x, b_y, a_x, a_y, cnt):
    n = len(board)
    m = len(board[0])
    dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
    if board[b_x][b_y] == 0:
        return 1, cnt
    winner = []
    loser = []
    check = False
    for i in range(4):
        nx, ny = b_x + dx[i], b_y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1:
            check = True
            board[b_x][b_y] = 0
            is_win, score = A_turn(board, a_x, a_y, nx, ny, cnt + 1)
            board[b_x][b_y] = 1
            if is_win:
                winner.append(score)
            else:
                loser.append(score)
    if check:
        if winner:
            return 0, min(winner)
        else:
            return 1, max(loser)
    else:
        return 1, cnt
def solution(board, aloc, bloc):
    cnt = 0
    a_x, a_y, b_x, b_y = aloc[0], aloc[1], bloc[0], bloc[1]
    _, answer = A_turn(board, a_x, a_y, b_x, b_y, cnt)
    return answer
print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2]))