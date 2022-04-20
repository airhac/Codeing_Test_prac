loc = input()
x = int(loc[1])
y = int(ord(loc[0])) - int(ord('a')) + 1
cnt = 0

cases = [(2, -1),(2, 1),(-2, 1),(-2, -1),(1, 2),(1, -2),(-1, 2),(-1, -2)]
#이 문제 같은 경우 원래 갈수 있는 경로의 경우의 수가 정해져있는데 그 이외로 되지 않으면 하나 씩 제거하는 결국 그 조건 안에 있는 경우만 카운트 해주면 된다.
for case in cases:
    xn = x + case[0]
    yn = y + case[1]
    if xn >0 and xn <9 and yn >0 and yn <9:
        cnt +=1

print(cnt)