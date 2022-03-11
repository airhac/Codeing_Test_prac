import sys
cnt = 0
def func(i):#한수 찾는 함수
    if i//100 == 0:
        return True
    else:
        s = map(int,list(str(i)))
        s = list(s)
        d = s[1] - s[0]
        if s[2] == s[1] + d:
            return True
        else:
            return False
                     
N = sys.stdin.readline()       
for i in range(1,int(N)+1):
    if func(i) == True:
        cnt+=1
        
print(cnt)

