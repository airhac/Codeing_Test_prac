#######효율성에 엄청난 시간초과가 뜸
# def solution(stones, k):
#     INF = int(1e9)
#     answer = INF
#     for i in range(len(stones) - k + 1):
#         maximum = 0
#         for stone in stones[i:i + k]:
#             if maximum < stone:
#                 maximum = stone
#         if maximum < answer:
#             answer = maximum
#     return answer
########이분탐색으로 문제 풀이
def solution(stones, k):
    start = 1
    end = 200000000
    while start <= end:
        mid = (start + end) // 2 #이값의 학생이 지나 간다고한 경우
        cnt = 0
        #이건 중간에 cnt가 k보다 커지는 경우가 있을때 break를 하므로 시간 복잡도가 O(n)이 아니다
        #그러므로 stone - mid부분을 전에 for문으로 돌려주면 시간 복잡도가 while안에서 O(n) 시간 복잡도를 가지면서 효율성이 통과가 되지 않았습니다.
        for stone in stones:
            if stone - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if k <= cnt:
                break
        if k <= cnt:
            end = mid - 1
        else:  
            start = mid + 1   
    return start
print(solution(	[2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))