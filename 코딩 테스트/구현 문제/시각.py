#내가 풀어본 방식
# N = int(input())
# cnt = 0
# sec = 0
# min = 0
# hour = 0
# while True:
#     if hour == N+1:
#         break
#     sec += 1
    
#     if sec == 60:
#         sec = 0
#         min += 1
#     if min == 60:
#         min = 0
#         hour +=1
    
#     if hour == 3 or min//10 ==3 or min%10 == 3 or sec//10 ==3 or sec%10 == 3:
#         cnt+=1

# print(cnt)

#이 문젠는 모든 경우를 다 일일이 확인해봐야하는 경우로 완전 탐색이며 완전 탐색은 데이터의 개수가 100만 개 이하일 때 사용하면 졸다.
#이 문제 경우 총 데이터의 개수가 86400개 밖에 없으므로 완전 탐색을 사용해도 괜찮다.
N = int(input())
cnt = 0
for h in range(N + 1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                cnt +=1
print(cnt)