########동적 할당으로 풀수 있는 문제 입니다.
#이문제는 제일 처음 숫자를 뽑았을때와 두번째 숫자를 뽑았을떄 의 경우가 두가지 나옵니다.
#dp[i] = max(dp[i = 1], dp[i -2] + dp[i])
def solution(sticker):
    dp_1 = [0] + [sticker[i] for i in range(len(sticker) - 1)]
    dp_2 = [0] + [sticker[i] for i in range(1, len(sticker))]
    for i in range(1, len(sticker)):
        if i == 1:
            dp_1[i] = max(dp_1[i], dp_1[i - 1])
        else:
            dp_1[i] = max(dp_1[i-1], dp_1[i-2] + dp_1[i])
    for i in range(1, len(sticker)):
        if i == 1:
            dp_2[i] = max(dp_2[i], dp_2[i - 1])
        else:
            dp_2[i] = max(dp_2[i-1], dp_2[i  - 2] + dp_2[i])
    if len(sticker) != 1:
        return max(dp_1[-1], dp_2[-1])
    else:
        return sticker[0]