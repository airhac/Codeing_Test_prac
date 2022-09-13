#left부터 right까지 최대 시간은 O(10 ^ 5)이다
def solution(n, left, right):
    answer = []
    num = 0
    for i in range(left, right + 1):
        div_num = i // n
        mod_num = i % n
        if div_num >= mod_num:
            answer.append(div_num + 1)
        else:
            answer.append(mod_num + 1)
    return answer
