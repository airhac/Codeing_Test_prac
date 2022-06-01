def possible(answer):
    for x, y, a in answer:
        #기둥을 설치할때
        if a == 0:
            #박닥일때, 밑에 보가 있을때, 그냥 기둥일때 
            if y == 0 or [x-1,y, 1] in answer or [x, y-1 , 0] in answer or [x, y, 1] in answer:
                continue
            return False
        #보를 설치할때
        elif a == 1:
            if y == 0 or ([x-1, y , 1] in answer and [x+1, y, 1] in answer) or [x+1, y-1 ,0] in answer or [x, y-1 , 0] in answer:
                continue
            return False
    return True
def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, a, b = frame
        if b == 0:#철거할경우
            answer.remove([x,y,a])
            if not possible(answer):
                answer.append([x,y,a])
        if b == 1:#설치할경우
            answer.append([x,y,a])
            if not possible:
                answer.remove([x,y,a])
    return sorted(answer)

n= 5
build_frame = 	[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

print(solution(n, build_frame))