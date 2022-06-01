# from copy import deepcopy
# from itertools import permutations
# def solution(n, weak, dist):
#     answer = len(dist) + 1
#     length = len(weak)
#     #원형인 경우 선형으로 만들어 주는데 문제에서 쌍방향을 전부다 고려해야한다고 했으므로 벽의 길이의 두배로만 만들어주고 각 위치의 길이만큼 더해준값을 넣어주면 된다.
#     #이러한 식으로하면 쌍방향을 모두 고려할 수 있습니다.
#     #ex) 1,5,6,10,13,17,18,22 
#     for i in range(length):
#         weak.append(weak[i] + n)
        
#     for start in range(length):#0, 1, 2, 3
#         for cases in list(permutations(dist, len(dist))):    
#             count = 1
#             position = weak[start] + cases[count -1] #현재 사람이 갈수있는 위치
#             for dir in range(start, start + length ):#여기서는 갈수 있는 위치까지 몇개의 취약점이 있나 확인 그래서 취약점만큼 돌아야한다. 취약점은 다 확인이 되어야하고 다 확인이 되면 그때 최저값을 반환
#                 if position < weak[dir]: #position이 waek[dir] 보다 작으면 취약점이 현재 사람으로써는 count만큼만 확인 가능하다는 뜻
#                     count+=1
#                     if count > len(dist): #여기서 count가 length보다 커지면 더이상 취약점을 확인 할 수 없다는 뜻
#                         break
#                     #그 다음 취약점에서 다음사람의 갈수 있는 시간만큼 더해주면 그 사람이 갈 수 있는 최대의 위치를 알수 있다.
#                     #사람이 바뀌었으니 count로 case도 바꿔 줍니다.
#                     #여기서 변해야하는 변수가 수동으로 변하는지 자동으로 변하는지 알면 반복문을 어디에 사용해야할지도 알수 있습니다
#                     position = weak[dir] + cases[count -1]
#             answer = min(answer, count)
#     if answer > len(dist):
#         return -1
#     return answer
#다른 풀이 순열조합을 사용하지만 풀이가 다름
# from itertools import permutations

# def solution(n, weak, dist):
#     answer = len(dist) + 1
#     length = len(weak)
#     result = []
#     weak_point = weak + [w + n for w in weak]
#     #어느 한 취약점에서 시작
#     for i, start in enumerate(weak): # (0, 1),(1, 5),(2, 6),(3, 10)
#         for friends in permutations(dist, len(dist)):#친구들로 구성할 수 있는 모든 경우의 수
#             count = 1
#             position = start
#             #이러한 식으로 돌리면 count가 len(dist)를 넘어갈 일은 없다.
#             for friend in friends:
#                 #시작 부분에서 현재 경우의 수의 시간만큼 더해줍니다
#                 position+=friend
#                 #더한값이 한 친구가 갈 수 있는 거리인데 그 값보다 작을시에 count를 더해줍니다.
#                 if position < weak_point[i + length - 1]:
#                     count+=1
#                     #weak_point에서 5~10(index = 1 ~ 3)
#                     postion = [w for w in weak_point[i+1:i+length]
#                                if w > postion][0]
#                 else:#마지막 취약점까지 도달
#                     result.append(count)
#                     break
#     return min(result) if result else -1
                    
                

# n = 12
# weak = [1, 5, 6, 10]
# dist = [1, 2, 3, 4]

# print(solution(n, weak, dist))
#set()을 이용한 풀이
def solution(n, weak, dist):
    count = 0
    repair_list=[()]#공집합문제를 해결해주기위해서 
    wl = len(weak)
    dl = len(dist)
    dist.sort(reverse=True)
    
    #고칠수 있는것을 리스트로 작성함으로써 count를 해주고 리스트의 크기가 원래 dist의 크기와 같아지면 return 해줍니다.
    for can_m in dist:#4,3,2,1
        count+=1
        repairs = []
        #수리가능한거만 확인해서 모은다
        for i, w in enumerate(weak):
            ends = weak[i:] + [n + nw for nw in weak[:i]]
            can = [end % n for end in ends if end - w <= can_m]
            repairs.append(set(can))
        #수리 가능한 경우 탐색
        
        cand = set()
        for repair in repairs:#repair도 set형식으로 넣어져 있어서 비교가능
            #수리한 리스트에 있으면 안넣고 있는경우 리스트에 삽입
            for x in repair_list:
                new = repair | set(x)
                if len(new) == wl:
                    return count
                cand.add(tuple(new))
        repair_list = cand
    return -1

n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]

print(solution(n, weak, dist))