from collections import deque
def solution(board, r, c):
    dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
    def check_line(x, y, dir, board):
        while True:
            x, y = x + dx[dir],y + dy[dir]
            if 0 <= x < 4 and 0 <= y < 4:
                if board[4 * x + y] != '0':
                    return x, y
            else:
                return x - dx[dir], y - dy[dir]
    board = ''.join(str(a) for b in board for a in b)
    
    q = deque([(r, c, -1, 0, board)]) 
    visited = set()
    while q:
        x, y, check, cnt, board = q.popleft()
        if board.count('0') == 16:
            return cnt      
        if (x, y, check, board) in visited:
            continue
        visited.add((x, y, check, board))
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 4 and 0 <= ny < 4:
                q.append((nx, ny, check, cnt + 1, board))
                c_x, c_y = check_line(x, y, i, board)
                q.append((c_x, c_y, check, cnt + 1, board))
        #endter 하는 경우
        location = 4 * x + y
        if board[location] != '0':
            if check == -1:
                q.append((x, y, location, cnt + 1, board))#board의 값이 0이 아니지만 앞면으로 된 카드가 없는경우 앞면으로 뒤집어야한다. 그러므로 [ENTER]를 하고 check응 이때 board위치를 넣어줍니다.
            elif board[check] == board[location] and check != location:
                board = board.replace(board[check], '0')
                q.append((x, y, -1, cnt + 1, board))

print(solution(	[[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0))