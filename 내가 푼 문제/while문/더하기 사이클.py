N = int(input())
n_cnt = 0
chk = N
while True:
    ten = chk//10
    one = chk%10
    chk = ten+one
    chk = int(str(one) + str(chk%10))
    n_cnt+=1
    if N == chk:
        break
print(n_cnt)