# s = list(map(int,list(input())))
# s.sort()
# result = 0
# for i in range(1,len(s)):
#     if s[i-1] == 0 or s[i-1] ==1:
#         s[i] = s[i-1] + s[i]
#     else:
#         s[i] = s[i-1]*s[i]
    
# print(s[len(s)-1])
#이문제는 굳이 리스트를 안써도 된다
s = input()
result = int(s[0])

for i in range(1, len(s)):
    n = int(s[i])#현재 위치해 있는 값
    if n <=1 or result <=1:
        result += n
    else:
        result *= n

print(result)