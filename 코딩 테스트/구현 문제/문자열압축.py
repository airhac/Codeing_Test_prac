# import time

# start_time = time.time()
# S = input()
# length = len(S)
# if length == 1:
#         cnum = 1
# else:
#     cnum = length // 2
# results = []

# for i in range(1,cnum+1):
#     c= 1
#     j = 0
#     s = []
#     while j < length:
#         if S[j:j+i] == S[j+i:j+2*i]:
#             c+=1
#         else:
#             if c == 1:
#                 s.append(S[j:j+i])
#                 c=1
#             else:
#                 s.append(str(c))
#                 s.append(S[j:j+i])
#                 c=1
#         j+=i       
#     result = ''.join(s)      
#     results.append(len(result))

# print(min(results))
# end_time = time.time()

# print('time:{}'.format(end_time - start_time))
#테스트 케이스의 경우 5번은 문자열 하나만 들어옵니다. 문자열이 하나인 경우 여기서는 전체길이의 반으로 반복문을 돌리므로 문자열이 하나인경우 for문이 돌지 않습니다. 그러므로
#문자열이 하나일때는 cnum을 1로 설정해주면 문제가 해결됩니다.
#현재 이 풀이는 min()를 쓰면 테스트중에서 하나가 통과되지가 않습니다.
#그래서 min()함수말고 비교연산자를 통한 최저값 구하기를 하니깐 통과가 됐습니다. 그런데 왜 이렇게 되는지는 아직 잘모릅니다
# def solution(s):

#     length = len(s)
#     cnum = length // 2
#     results = []

#     for i in range(1,cnum+1):
#         c= 1
#         j = 0
#         st  = []
#         while j < length:
#             if s[j:j+i] == s[j+i:j+2*i]:
#                 c+=1
#             else:
#                 if c == 1:
#                     st.append(s[j:j+i])
#                     c=1
#                 else:
#                     st.append(str(c))
#                     st.append(s[j:j+i])
#                     c=1
#             j+=i        
#         result = ''.join(st)      
#         results.append(result)
    
#     for el in results:
#         if len(el) < length and len(el) != 0:
#             length = len(el)
#     return length

# for j in range(div):
#         if S[j:j+i] == S[j+i:j+2*i]:
#             c+=1
#         else:
#             if c == 1:
#                 s.append(S[j:j+i])
#                 c=1
#             else:
#                 s.append(str(c))
#                 s.append(S[j:j+i])
#                 c=1
#     s.append(str(c))
#     s.append(S[j:j+i])   
#     print(s)
#프로그래머스의 다른사람 풀이
import time

start_time = time.time()
def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

a = [
    "aabbaccc"
]

for x in a:
    print(solution(x))
end_time = time.time()

print('time:{}'.format(end_time - start_time))