N = int(input())
array = [0] * 1000001
for i in input().split():
    array[int(i)] = 1

M = int(input())
order = list(map(int, input().split()))

for i in order:
    if array[i] == 1:
        print('yes', end =' ')
    else:
        print('no', end =' ')