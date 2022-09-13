#역으로 돌아가면서 최종 위치로 올수있는 칸들을 찾습니다.
def solution(n, m, x, y, queries):
    answer = 0
    top, bottom, left, right = x, x, y, y
    for d, dx in queries[::-1]: 
        if d == 0:
            if right + dx < m:
                temp = right + dx
            else:
                temp = m - 1
            right = temp
            if left != 0:
                left = left + dx
        elif d == 1:
            if left - dx >= 0:
                temp = left - dx
            else:
                temp = 0
                
            left = temp
            if right != m - 1: 
                right = right - dx
        elif d == 2:
            if bottom + dx < n:
                temp = bottom + dx
            else:
                temp = n - 1
                
            bottom = temp
            if top != 0:
                top = top + dx
                
        elif d == 3:
            if top - dx >= 0:
                temp = top - dx
            else:
                temp = 0
                
            top = temp
            if bottom != n - 1:
                bottom = bottom - dx
            
        if left > m - 1 or right < 0 or top > n - 1 or bottom < 0:
            break
    else:
        answer = ((bottom - top) + 1) * ((right - left) + 1) 
    return answer
print(solution(2, 2, 0, 0, [[2, 1], [0, 1], [1, 1], [0, 1], [2, 1]]))