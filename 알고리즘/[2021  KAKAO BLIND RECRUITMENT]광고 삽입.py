def change_time(time , check):
    if check:
        h, m, s = map(int, time.split(':'))
        time = (h * 60 * 60) + (m * 60) + s
        return time
    else:
        h = str(time // 3600)
        time %= 3600
        m = str(time // 60)
        time %= 60
        s = str(time)
        return h.zfill(2) + ':' + m.zfill(2) + ':' + s.zfill(2)
    
def solution(play_time, adv_time, logs):
    dp = [0] * (change_time(play_time, True) + 1)
    answer = []#각 시작부터 adv를 재생할때 마다 누적 재생시간을 담아 줍니다
    for log in logs:
        start, end = log.split('-')
        start = change_time(start, True)
        end = change_time(end, True)
        dp[start] += 1
        dp[end] -= 1
    
    
    for i in range(1, change_time(play_time, True)):
        dp[i] += dp[i - 1]
    for i in range(1, change_time(play_time, True)):
        dp[i] += dp[i - 1]
    answer = []
    for log in logs:
        start, end = log.split('-')
        start = change_time(start, True)
        adv = change_time(adv_time, True)
        
        answer.append(dp[adv] - dp[start] + 1)
    print(answer)  
    return 0

print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"]))

