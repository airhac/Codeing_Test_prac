import sys
input = sys.stdin.readline
word = input().strip()
dp = [0] * 9
for i in range(len(word)):
    index = int(word[i])
    if index == 9:
        index = 6
    dp[index] += 1
dp[6] = (dp[6] + 1) // 2
print(max(dp))