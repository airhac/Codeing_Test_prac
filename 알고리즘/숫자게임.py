def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    a_index = 0
    b_index = 0
    while b_index <= len(B) or a_index <= len(A):
    
        if A[a_index] < B[b_index]:
            a_index = b_index + 1 
            answer += 1
        else:
            b_index += 1
    return answer
print(solution([5,1,3,7], [2,2,6,8]))
#다른 사람이 푼 더 간단한 풀이
#나와 같이 sort를 하였지만 for문을 이용하여 풀었다
def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    j = 0

    for i in range(len(A)):
        if A[j] < B[i]:
            answer = answer + 1
            j = j+1

    return answer