def solution(arr):
    answer = [0, 0]
    length = len(arr)
    
    def quard(a, b, l):
        check = arr[a][b]
        for i in range(a, a + l):
            for j in range(b, b + l):
                if check != arr[i][j]:
                    l //= 2
                    quard(a, b, l)
                    quard(a, b + l, l)
                    quard(a + l, b, l)
                    quard(a + l, b + l, l)
                    return
        answer[check] += 1
    quard(0, 0, length)
    return answer
print(solution(	[[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]))