#소수 여부 판별
import math
def possible(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
def solution(n, k):
    answer = 0
    k_number = ''
    #k진수로 만들기
    while True:
        if n == 0:
            break
        mod = n % k
        k_number += str(mod)
        n //= k
     
    for s in k_number[::-1].split('0'):
        if s != '' and s != '1':
            if possible(int(s)):
                answer += 1
    return answer