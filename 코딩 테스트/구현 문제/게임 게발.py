N, M = map(int, input().split())
dx, dy, d = map( int, input().split())
g_map = []
for n in range(N):
    row = list(map(int,input().split()))
    g_map.append(row)

ver = [-1, 0, 1, 0]
hor = [0, 1, 0, -1]
car = [0, 1, 2 , 3]

result = 0
while True:
    cnt = 0
    result +=1
    g_map[dx][dy] = 1
    
    for _ in range(len(car)):
        if d == -1:
            d=3
        xn = dx + hor[d]
        yn = dy + ver[d]
        
        if g_map[xn][yn] == 1 or xn <=0 or xn >M or yn <=0 or yn >N:
            d-=1
            cnt+=1
            continue
        dx = xn
        dy = yn
        
        break
    
    if cnt == 4:
        break
    
        
print(result)  
        
        
        
        
        