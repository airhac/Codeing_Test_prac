import sys
input = sys.stdin.readline

for t in range(int(input())):
    string = list(input().strip())
    dict = {')' : '('}
    stack = []
    if string[0] ==')':
        print('NO')
        continue
    for s in string:
        if stack:
            if s in dict and stack[-1] == dict[s]:
                stack.pop()
            else:
                stack.append(s)
        else:
            stack.append(s)
    
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')