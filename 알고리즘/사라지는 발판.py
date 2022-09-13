###########33
def A_turn(board, a_x, a_y, b_x, b_y, cnt):
    n = len(board)
    m = len(board[0])
    winner = []
    loser = []
    dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
    if board[a_x][a_y] == 0:
        return 1, cnt
    check = False #check변수는 앞으로 한칸을 갔을때 갈곳이 없으면 Flase, 갈곳이 한군데라도 있으면 True 
    for i in range(4):
        nx, ny = a_x + dx[i], a_y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1:
            check =  True
            board[a_x][a_y] = 0
            iswin, score = B_turn(board, b_x, b_y, nx, ny, cnt + 1)
            board[a_x][a_y] = 1
            if iswin:#A가 이겼을때
                winner.append(score)
            else:
                #A가 졌을떄
                loser.append(score)
    if check:
        if winner:#b가 이겼으니 나는 패배를 반환 합니다.
            return 0, min(winner)
        else:
            return 1, max(loser)
    else:#더이상 나아갈 수 없을떄 반환을 해줍니다. 
        return 1, cnt 
                  
def B_turn(board, b_x, b_y, a_x, a_y, cnt):
    n = len(board)
    m = len(board[0])
    winner = []
    loser = []
    dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
    if board[b_x][b_y] == 0:
        return 1, cnt
    check = False
    for i in range(4):
        nx, ny = b_x + dx[i], b_y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1:
            check = True
            board[b_x][b_y] = 0
            iswin, score = A_turn(board, a_x, a_y, nx, ny, cnt + 1)
            board[b_x][b_y] = 1
            if iswin:
                #B가 이겼을때
                winner.append(score)
            else:
                #B가 졌을때
                loser.append(score)
    if check:
        #a가 이겼으니 나는 패배를 반환 합니다.
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
############33333

print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2]))