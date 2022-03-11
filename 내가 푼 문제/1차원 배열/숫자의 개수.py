A = int(input())
B = int(input())
C = int(input())

num = str(A * B * C)

def count(num):
    cnt = [0]*10
    for i in range(len(num)):
        if int(num[i]) == 0:
            cnt[0] +=1
        elif int(num[i]) == 1:
            cnt[1] +=1
        elif int(num[i]) == 2:
            cnt[2] +=1
        elif int(num[i]) == 3:
            cnt[3] +=1
        elif int(num[i]) == 4:
            cnt[4] +=1
        elif int(num[i]) == 5:
            cnt[5] +=1
        elif int(num[i]) == 6:
            cnt[6] +=1
        elif int(num[i]) == 7:
            cnt[7] +=1
        elif int(num[i]) == 8:
            cnt[8] +=1
        elif int(num[i]) == 9:
            cnt[9] +=1
    return cnt

for i in count(num):
    print(i)

#python 에는 count함수가 있다. 이 함수를 쓰면 제일 빠르다