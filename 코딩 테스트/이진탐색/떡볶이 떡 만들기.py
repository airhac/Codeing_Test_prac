#파라메틱 서치 문제는 반복문으로도 문제를 해결할 수 있다
N, M = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

start = 0
end = max(array)
result = 0
while start <= end:
    mid = (start + end) // 2
    price = 0
    for i in array:
        if i > mid:
            price += i - mid
    if price <  M:
        end = mid -1
    else:
        result = mid
        start = mid + 1
        
print(result)