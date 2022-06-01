# def solution(food_times, k):
#     answer = 0
#     s = 0
#     for i in food_times:
#         s += i
#     while k!=0:
#         answer = answer % len(food_times)
#         if food_times[answer] != 0:
#             k-=1
#             food_times[answer]-=1
#             answer+=1
#             s-=1
#         else:
#             answer+=1
#         if s == 0:
#             resturn -1
            
#     return answer % len(food_times) + 1
#일단 다른거 생각 안하고 while 반복문만을 사용했을때 방법
#답은 나오나 효율성에 문제가 있음
#이번 문제는 동적 할당을 사용
#정렬을 이용한 방법
# import heapq

# def solution(food_times, k):
#     if sum(food_times) <= k:
#         return -1
#     size = len(food_times)
#     q=[]
#     for i in range(size):
#         heapq.heappush(q , (food_times[i], i+1))
#     begin = 0
#     spend = 0
    
#     while spend + ((q[0][0] - begin)*size) <= k:
#         now = heapq.heappop(q)[0]
#         spend += (now - begin) * size
#         begin = now
#         size-=1
#     result = sorted(q, key = lambda x : x[1])
#     print(result)
#     return result[(k-spend) % size][1]
        

# print(solution([3, 1, 2], 5))
# from operator import itemgetter
# def solution(food_times, k):
#     answer = 0
#     foods = []
#     n = len(food_times)
#     for i in range(n):
#         foods.append((food_times[i], i+1))
#     foods.sort()

#     pretime = 0    
#     for i, food in enumerate(foods):
#         diff = food[0] - pretime
#         if diff != 0:
#             spend = n * diff
#             if spend <= k:
#                 k-=spend
#                 pretime = food[0]
#             else:
#                 k%=n
#                 sublist = sorted(foods[i:], key = itemgetter(1))
#                 return sublist[k][1]
#         n-=1
#     return -1
# import heapq

# def solution(food_times, k):
#     #make heap
#     heap = []
#     for i in range(len(food_times)):
#         heapq.heappush(heap, (food_times[i], i+1))
#     #find k
#     temp = 0
#     while(heap):
#         now = heap[0][0] - temp
#         new_k = k - (now * len(heap))
#         if new_k < 0:
#             break
#         heapq.heappop(heap)
#         k = new_k
#         temp += now
#     #check empty
#     if not heap: return -1
#     #find index
#     heap.sort(key=lambda x : x[1])
#     return heap[k%len(heap)][1]