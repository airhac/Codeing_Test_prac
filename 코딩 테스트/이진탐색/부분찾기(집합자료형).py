N = int(input())
market = set(map(int, input().split()))

M = int(input())
order = list(map(int, input().split()))

for i in order:
    if i in market:
        print('yes', end = ' ')
    else:
        print('no' , end = ' ')