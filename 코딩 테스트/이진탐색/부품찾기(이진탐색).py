from tkinter.messagebox import YES


def binary_search(array, target, start, end):
    mid = (start + end)//2
    while start >= end:
        if array[mid] > target:
            end = N - 1
        elif array[mid] < target:
            start = N + 1
        else:
            return mid
    return  None
        
N = int(input())
market = list(map(int, input().split()))
market.sort()
M = int(input())
order = list(map(int, input().split()))

for o in range(len(order)):
    result = binary_search(market, o, 0, N)
    if result != None:
        print('yes' , end ='')
    else:
        print('no', end='')