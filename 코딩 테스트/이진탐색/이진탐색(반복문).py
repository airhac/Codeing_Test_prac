def binary_search(array, target, start, end):
    while start <= end:
        h = (start + end)//2
        if array[h] == target:
            return h
        elif array[h] > target:
            end = h-1
        else:
            start = h + 1
        return None
    

N ,target =  map(int, input().split())
array = list(map(int, input().split()))


result = binary_search(array, target, 0, N-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
    