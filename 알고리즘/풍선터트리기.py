def solution(a):
    answer = [False]*len(a)
    
    front, back = int(1e9), int(1e9)
    
    for i in range(len(a)):
        if a[i] < front:
            front = a[i]
            answer[i] = True
        
        if a[-1-i] < back:
            back = a[-1-i]
            answer[-1-i] = True
        
    return sum(answer)