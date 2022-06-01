def binary_search(array, target, start, end):
    h = (start + end)//2
    if start > end:
        return None
    if array[h] == target:
        return h
    if array[h] > target:
        return binary_search(array, target, start, h - 1)
    elif array[h] < target:
        return binary_search(array, target, h + 1, end)
    

N ,target =  map(int, input().split())
array = list(map(int, input().split()))


result = binary_search(array, target, 0, N-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
    
