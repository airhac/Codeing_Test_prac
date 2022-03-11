import sys
for t in range(int(input())):
    a, b = map(int, sys.stdin.readline().split())
    print('Case #{}: {} + {} = {}'.format(t+1, a, b, a+b))