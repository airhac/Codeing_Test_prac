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

#######################3
# def solution(play, adv, logs):
#     c = lambda t: int(t[0:2]) * 3600 + int(t[3:5]) * 60 + int(t[6:8])
#     play, adv = c(play), c(adv)
#     logs = sorted([s for t in logs for s in [(c(t[:8]), 1), (c(t[9:]), 0)]])

#     v, p, b = 0, 0, [0] * play
#     for t, m in logs:
#         if v > 0:
#             b[p:t] = [v] * (t - p)
#         v, p = v + (1 if m else -1), t

#     mv, mi = (s := sum(b[:adv]), 0)
#     for i, j in zip(range(play - adv), range(adv, play)):
#         s += b[j] - b[i]
#         if s > mv:
#             mv, mi = s, i + 1

# #     return f"{mi//3600:02d}:{mi%3600//60:02d}:{mi%60:02d}"
# print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"]))
######################3
def s2i(s):
    z = s.split(':')
    return int(z[0])*3600+int(z[1])*60+int(z[2])

def i2s(t):
    ret = ''
    ret += str(t//3600).zfill(2)+':'
    t %= 3600
    ret += str(t//60).zfill(2)+':'
    t %= 60
    ret += str(t).zfill(2)
    return ret

def solution(play_time, adv_time, logs):
    pt, at = s2i(play_time), s2i(adv_time)
    d = [0]*360001
    for l in logs:
        st, en = map(s2i, l.split('-'))
        d[st] += 1
        d[en] -= 1
    for i in range(1, 360001):
        d[i] += d[i-1]
    mxval, mxtime = sum(d[:at]), 0
    curval = mxval
    for i in range(1, 360001-at):
        curval = curval - d[i-1] + d[i+at-1]#그때 마다의 누적 시간을 바꾼다.
        if curval > mxval:
            mxval = curval
            mxtime = i
    return i2s(mxtime)
print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"]))