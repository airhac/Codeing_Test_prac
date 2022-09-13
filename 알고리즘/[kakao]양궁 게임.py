from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1]
    table = [i for i in range(11)]
    max_diff = 0
    for cases in combinations_with_replacement(table, n):
        diff = 0
        a_score = 0
        r_score = 0
        l = [0] * 11
        for case in cases:
            l[10 - case] += 1
        
        for index, val in enumerate(zip(info, l)):
            a, r = val
            if a == 0 and r == 0:
                continue
            if r <= a:
                a_score += (10 - index)
            else:
                r_score += (10 - index)
        
        if r_score > a_score:
            diff = r_score - a_score
            if diff > max_diff:
                max_diff = diff
                answer = l
    
    return answer

print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))