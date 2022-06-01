N = int(input())

food = list(map(int, input().split()))

d = [0] * 301

d[0] = food[0]
d[1] = max(food[0],food[1])#3부터는 앞에 두개를 아무거나 털수 있으니 

for i in range(2,N):
    d[i] = max(d[i-1],food[i] + d[i-2])
print(d[N])