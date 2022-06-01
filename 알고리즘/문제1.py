def solution(atmos):
    answer = 0
    day = 0
    for i in atmos:
        print(day)
        #대기 상태가 안좋을때
        if i[0] >80 or i [1]>35:
            #대기상태가 둘다 매우 나쁨일때
            if i[0] > 150 and i[1] > 75:
                #필요한 마스크양을 늘리고 날짜를 초기화해줍니다.
                answer+=1
                day=0
            elif day ==2:
                day=0
            #대기상태가 안좋을때 마스크를 한번 씁니다.
            elif day == 1:
                answer+=1
                day+=1
            else:
                day+=1
        #대기 상태가 좋을때
        else:
            if day == 2:
                day=0
            elif day == 1:
                answer+=1
                day+=1
            else:
                continue
        
    return answer

print(solution([[140, 90], [177, 75], [95, 45], [71, 31], [150, 30], [80, 35], [72, 33], [166, 81], [151, 75]]))