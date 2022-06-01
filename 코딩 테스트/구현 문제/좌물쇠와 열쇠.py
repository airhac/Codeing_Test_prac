def solution(key, lock):
    lock_len = len(lock)
    key_len = len(key) 
    width = lock_len + 2* (key_len-1)
    #좌물쇠를 check할 전체 그래프 생성
    graph = [[0] * width for _ in range(width)]
    for i in range(lock_len):
        for j in range(lock_len):
            graph[i + (key_len -1)][j + (key_len-1)] = lock[i][j]
    
    #90도씩회전을 시키면서 확인
    for _ in range(4):
        check_len = lock_len + (key_len-1)
        key = rotation(key)
        #각 키는 check_len의 길이만큼 확인해야 전체 맞추는것이 가능한지 확인 할 수 있습니다.
        #키와 좌물쇠가 겹치는 부분이 생기면 더해줍니다.
        for i in range(check_len):
            for j in range(check_len):
                #키 끼워 맞추기
                for k in range(key_len):
                    for l in range(key_len):
                        graph[i + k][j + l] += key[k][l]
                if key_check(graph, key_len) == True:
                    return True
                for k in range(key_len):
                    for l in range(key_len):
                        graph[i + k][j + l] -= key[k][l]    
    return False
#형렬을 회전 시키는 규칙은 i는 j로 바뀌고 j는 원래 키길이-i-1값으로 바뀐다.
def rotation(key):
    key_len = len(key)
    new_key = [[0]*key_len for _ in range(key_len)]
    for i in range(key_len):
        for j in range(key_len):
            new_key[j][key_len-i-1] = key[i][j]
    return new_key
#현재 들어온 lock과 key가 일치하는지 확인하는 과정
def key_check(new_lock,key_len):
    length = len(new_lock) - 2*(key_len -1)
    for i in range(length):
        for j in range(length):
            if  new_lock[i+(key_len-1)][j + (key_len-1)] != 1:
                return False
    return True
key = [[0,0,0],
       [1,0,0],
       [0,1,1]]
lock = [[1,1,1],
        [1,1,0],
        [1,0,1]]

print(solution(key,lock))
#프로그래머스에서 다른사람 풀이
# def solution(key, lock):
#     N = len(lock)
#     v, vac = vacant(lock)
#     if not vac: return True
#     vac = vac[0]
#     find = False
#     for key in rotate(key):
#         for i in range(len(key)):
#             cnt = 0
#             rr, cc = vac[0]-key[i][0], vac[1]-key[i][1]
#             print(rr, cc)
#             for j in range(i, len(key)):
#                 r, c = key[j]
#                 r, c = r+rr, c+cc
#                 if not (0 <= r < N and 0 <= c < N): continue
#                 if lock[r][c] == 1: break
#                 cnt += 1
#             if cnt == v:
#                 find = True
#                 break
#         if find: break
#     if find: return True
#     return False


# def vacant(lock):
#     N = len(lock)
#     vac = []
#     v = 0
#     for r in range(N):
#         for c in range(N):
#             if lock[r][c] == 0:
#                 vac.append((r, c))
#                 v += 1
#     return v, vac


# def rotate(key):
#     M = len(key)
#     key1 = [(r, c) for r in range(M) for c in range(M) if key[r][c] == 1]
#     key2 = [(M-r-1, c) for c, r in key1]
#     key3 = [(r, M-c-1) for c, r in key1]
#     key4 = [(M-r-1, M-c-1) for r, c in key1]

#     key1 = quick_sort(key1)
#     key2 = quick_sort(key2)
#     key3 = quick_sort(key3)
#     key4 = quick_sort(key4)
#     print(key1, key2, key3, key4)

#     return key1, key2, key3, key4


# def quick_sort(arr):
#     if not arr: return []
#     pivot = arr[len(arr)//2]
#     lesser, equal, greater = [], [pivot], []

#     for pos in arr:
#         if pos[0] < pivot[0]:
#             lesser.append(pos)
#         elif pos[0] > pivot[0]:
#             greater.append(pos)
#         else:
#             if pos[1] < pivot[1]:
#                 lesser.append(pos)
#             elif pos[1] > pivot[1]:
#                 greater.append(pos)

#     return quick_sort(lesser) + equal + quick_sort(greater)