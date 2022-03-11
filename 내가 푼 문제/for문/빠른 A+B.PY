import sys
# sys.stdin.readline 문자열을 받을 시 .rstrip()을 사용
for t in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    sys.stdout.write(f"{a + b}\n")
