from collections import defaultdict
import sys
input = sys.stdin.readline

n = 0

dict = defaultdict(int)
while True:
    tree = input().rstrip()
    if not tree:
        break
    dict[tree] += 1
    n += 1

s_tree = list(dict.keys())
s_tree.sort()
for tree in s_tree:
    print('{0} {1:0.4f}'.format(tree , dict[tree]/n))