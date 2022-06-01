def get_time(time):
    div_time = time.split(':')
    hour = int(div_time[0]) * 3600
    min = int(div_time[1]) * 60
    sec = list(map(int,div_time[2].split('.')))
    
    end_time  = ((hour + min + sec[0]) * 1000) + sec[1]
    return end_time
def get_start_time(time, diff):
    pro_time = int(float(diff[:-1])*1000)
    return get_time(time) - pro_time + 1
#실수는 오차 범위가 생기므로 왠만하면 정수로 계산해주는것이 좋다
def solution(lines):
    answer = 0
    end_time = []
    start_time = []
    
    for line in lines:
        time = line.split(' ')[1]
        diff = line.split(' ')[2]
        # time = 2016-09-15 20:59:57.421 , diif = 0.351s
        end_time.append(get_time(time))
        start_time.append(get_start_time(time, diff))
    
    for i in range(len(lines)):
        cnt = 0
        cur_end_time = end_time[i] + 1000 -1
        for j in range(i,len(lines)):
            if start_time[j] <= cur_end_time:
                cnt+=1
        
        answer = max(answer, cnt)
    return answer

lines = [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]

print(solution(lines))