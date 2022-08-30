import sys
import math
input = sys.stdin.readline
tri = []
result = []
for _ in range(3):
    tri.append(list(map(int, input().split())))
x1, y1 = tri[0][0], tri[0][1]
x2, y2 = tri[1][0], tri[1][1]
x3, y3 = tri[2][0], tri[2][1]

if (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3) == 0:
    result.append('X')
else:
    side = []
    side.append(math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2)))
    side.append(math.sqrt(math.pow((x3 - x2), 2) + math.pow((y3 - y2), 2)))
    side.append(math.sqrt(math.pow((x1 - x3), 2) + math.pow((y1 - y3), 2)))
    side.sort()
    
    if side[0] == side[1] and side[1] == side[2] and side[2] == side[0]:
        result.append('JungTriangle')
    elif side[0] == side[1] or side[1] == side[2] or side[2] == side[0]:
        if math.sqrt(math.pow(side[0], 2) + math.pow(side[1], 2)) == side[2]:
            result.append('Jikkak2Triangle')
        elif math.sqrt(math.pow(side[0], 2) + math.pow(side[1], 2)) > side[2]:
            result.append('Yeahkak2Triangle')
        else:
            result.append('Dunkak2Triangle')
    else:
        if math.sqrt(math.pow(side[0], 2) + math.pow(side[1], 2)) == side[2]:
            result.append('Jikkak2Triangle')
        elif math.sqrt(math.pow(side[0], 2) + math.pow(side[1], 2)) > side[2]:
            result.append('Yeahkak2Triangle')
        else:
            result.append('Dunkak2Triangle')

print(result[0])
