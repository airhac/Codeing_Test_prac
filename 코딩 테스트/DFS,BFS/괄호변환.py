# import sys
# input = sys.stdin.readline
# S = input()
def valenced_string(s):
    count = 0
    u = ''
    v = ''
    for i in range(len(s)):
        if s[i] == '(':
            count +=1
            u += s[i]
        elif s[i] ==')':
            count -=1
            u += s[i]
        if count == 0:
            u = s[:i + 1]
            v = s[i+1:]
            return u, v
    
def right_string(u):#u가 올바른 괄호형태인지 확인
    u = u[1:-1]
    for i in range(len(u)):
        if u[i] == '(':
            u = u[:i] + ')' + u[i + 1:] 
        elif u[i] == ')':
            u = u[:i] + '(' + u[i + 1:] 
    return u
def solution(S):
    result = 0
    index = 0
    if S != '':
        u, v = valenced_string(S)
        if u[0] == '(':
            S = u + solution(v)    
        else:
            S = '(' + solution(v) + ')' + right_string(u)
            
    return S



print(solution("()))((()"))