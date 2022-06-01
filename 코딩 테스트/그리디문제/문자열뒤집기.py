# s = input()
# result = s[0]
# cnt =0
# for i in range(1,len(s)):
#     if result != s[i]:
#         cnt+=1
    
# print(cnt//2)
s = input()
count0 = 0
count1 = 1
if s[0] == '1':
    count0 +=1 #1을 0으로 바꾸는 거니깐
else:
    count1 +=1
    
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '1':
            count0+=1
        else:
            count1+=1
            
print(min(count0, count1))
