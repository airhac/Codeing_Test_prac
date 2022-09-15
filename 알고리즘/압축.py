from collections import defaultdict
def solution(msg):
    answer = []
    book = defaultdict(int)
    for word in range(1, 27):
        book[chr(word + 64)] += word
    s = ''
    next_num = 27
    i = 0
    while i < len(msg):
        #사전에 없을때 까지 더한다
        s += msg[i]
        print(s)
        if s not in book:
            book[s] = next_num
            next_num += 1
            
            temp = s[:-1]
            answer.append(book[temp])
            s = ''
        else:
            i += 1
            continue
    answer.append(book[s])
    return answer
print(solution('KAKAO'))