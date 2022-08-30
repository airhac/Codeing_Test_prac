import sys
input = sys.stdin.readline
N, K = map(int, input().split())
stack = []
number = input().strip()
cnt = 0

for num in number:
    n = int(num)
    while stack and stack[-1] < n and cnt < K:
        stack.pop()
        cnt += 1
    stack.append(n)
        
print(''.join(list(map(str,stack))[:N - K]))

