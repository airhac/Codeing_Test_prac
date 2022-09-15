def solution(n, t, m, p):
    answer = ''
    string = '0'
    dic = { '10' : 'A', '11' : 'B', '12' : 'C', '13' : 'D', '14' : 'E', '15' : 'F'}
    num = 0
    for i in range(1, t * m + 1):
        while i > 0:
            num = i % n
            if  num < 10:
                string += str(num)
            else:
                string += dic[str(num)]
            i //= n
        print(string)
            
    return answer
print(solution(2, 4	,2,1))