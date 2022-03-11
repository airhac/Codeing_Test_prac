import sys
C = int(input())
results = []

for c in range(C):
    input = list(map(int, sys.stdin.readline().split()))
    num = input[0]
    scores = input[1:]
    mean = sum(scores)/num
    comp = [score for score in scores if score > mean]
    cal = (len(comp)/num)*100
    results.append(cal)

for result in results:
    print('{0:.3f}%'.format(result))
    


