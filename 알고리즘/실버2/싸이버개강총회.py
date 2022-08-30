import sys
from collections import defaultdict
input = sys.stdin.readline

S, E, Q = input().split()
S = int(S.split(':')[0]) * 60 + int(S.split(':')[1])
E = int(E.split(':')[0]) * 60 + int(E.split(':')[1])
Q = int(Q.split(':')[0]) * 60 + int(Q.split(':')[1])
check_list = defaultdict(list)
while True:
    check = input().strip()
    if not check:
        break
    time, student = check.split()
    h, m = map(int, time.split(':'))
    t = h * 60 + m
    if t <= S or E<= t <= Q:
        check_list[student].append(t)
answer = 0
for stu in check_list.items():
    if 2 <= len(stu[1]):
        if stu[1][0] <= S and E<= stu[1][-1] <= Q:
            answer += 1
print(answer)
