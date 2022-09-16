##공백이 여러개인 경우를 생각해줘야합니다
import re
def solution(s):
    answer = ''
    space = re.findall('[^a-zA-Z0-9]+', s) + ['']
    s = list(map(lambda x : x.capitalize(), s.split()))
    for a, b in zip(space, s):
        answer += (b + a)
    return answer
print(solution('a   a12aaa   1aaaa   aaaaaaa     a'))