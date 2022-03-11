S = list(input().upper())
s = list(set(S))

c = []
for i in s:
 c.append(S.count(i))

if c.count(max(c))>=2 and c.count(max(c))<len(S) :
    print('?')
else:
    print(s[c.index(int(max(c)))])