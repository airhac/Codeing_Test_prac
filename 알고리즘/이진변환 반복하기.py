from bisect import bisect_left
def solution(s):
    answer = []
    cycle = 0
    cnt = 0
    word = 0
    while word !=1:
        words = list(s)
        words.sort()
        index = bisect_left(words, '1')
        cnt += len(words[:index])#제거할 0의 경우
        print(cnt)
        word = len(words[index:])#0을 제거한 후 길이를 이진변화
        s = bin(word)[2:]
        cycle += 1
    return [cycle, cnt]

print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))