i = 1
data = set(range(1,10001))
result = set()
for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    result.add(i)
    

l = sorted(data - result)
for s in l:
    print(s)