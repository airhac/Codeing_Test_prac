# N = list(map(int, input()))

# mid = len(N)//2

# if sum(N[:mid]) == sum(N[mid:]):
#     print('LUCKY')
# else:
#     print('READY')

#풀이법2(파이썬의 sum()함수를 사용하지 않은 방법)
# n = list(map(int, input()))

# length = len(n)
# summary = 0
# for i in range(length//2):
#     summary += n[i]
# for i in range(length//2, length):
#     summary -= n[i]
    
# if summary == 0:
#     print('LUCKY')
# else:
#     print('READY')
    