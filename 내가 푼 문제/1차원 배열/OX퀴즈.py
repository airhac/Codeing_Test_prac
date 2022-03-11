N = int(input())
result = []
for _ in range(N):
    sum = 0
    cnt = 0
    answer = input()
    for i in list(answer):
        if i == 'O':
            cnt += 1
            sum += cnt
        else:
            cnt = 0
    
    result.append(sum)

for r in result:
    print(r)

