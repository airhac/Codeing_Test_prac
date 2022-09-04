def solution(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[2] = 3
    for i in range(4, n + 1, 2):
        dp[i] = 3 * dp[i - 2] + 2 * sum(dp[i - n] for n in range(4, n + 1, 2)) 
    return dp[n] % 1000000007
print(solution(12))
####