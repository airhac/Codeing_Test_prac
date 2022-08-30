R ,C, Q = map(int, input().split())
graph = [[0] * (C + 1)]

for i in range(1, R + 1):
    array = [0] + list(map(int, input().split()))
    for index in range(1, C + 1):
        array[index] += array[index - 1]
        if i > 1:
            array[index] += (graph[i - 1][index] - graph[i - 1][index - 1])
    graph.append(array)

ans = []
for t in range(Q):
    s = 0  
    x1, y1, x2, y2 = map(int, input().split())
    s = graph[x2][y2] - (graph[x2][y1 - 1] + graph[x1 - 1][y2]) + graph[x1 - 1][y1 - 1]
    tot = (x2 - x1 + 1) * (y2 - y1 + 1)
    ans.append(s // tot)
print('\n'.join(map(str, ans)))
# R ,C, Q = map(int, input().split())
# graph = [[0] * (C + 1)]
# s = 0
# for i in range(1, R + 1):
#     array = [0] + list(map(int, input().split()))
#     for index in range(1, C + 1):
#         array[index] += array[index - 1]
#     graph.append(array)
# for t in range(Q):
#     s = 0  
#     x1, y1, x2, y2 = map(int, input().split())
#     tot = (x2 - x1 + 1) * (y2 - y1 + 1)
#     for i in range(x1, x2 + 1):
#         s += (graph[i][y2] - graph[i][y1 - 1])
#     print(s // tot)
# #####################
# import sys; input = sys.stdin.readline
# from itertools import accumulate

# def main():
#     R, C, Q = map(int, input().split())
#     memo = [[0 for _ in range(C + 1)]]
#     for i in range(1, R + 1):
#         lst = [0]
#         lst.extend(map(int, input().split()))
#         memo.append(list(accumulate(lst)))

#     for i in range(1, R + 1):
#         for j in range(1, C + 1):
#             memo[i][j] += memo[i - 1][j]
#     for m in memo:
#         print(m)
#     ans = []
#     for _ in range(Q):
#         r1, c1, r2, c2 = map(int, input().split())
#         area = memo[r2][c2] - memo[r1 - 1][c2] - memo[r2][c1 - 1] + memo[r1 - 1][c1 - 1]
#         num_of_area = (r2 - r1 + 1) * (c2 - c1 + 1)
    #     ans.append(area // num_of_area)
    # print('\n'.join(map(str, ans)))


# if __name__ == "__main__":
#     main()
    
# ############################
# """Solution code for "BOJ 16507. 어두운 건 무서워".

# - Problem link: https://www.acmicpc.net/problem/16507
# - Solution link: http://www.teferi.net/ps/problems/boj/16507

# Tags: [Prefix sum]
# """

# import sys


# def create_2d_prefix_sum(nums):
#     prefix_sum = [[0] * (len(nums[0]) + 1)]
#     for row in nums:
#         prefix_sum.append([ps := 0] +
#                           [(ps := ps + num) + p
#                            for num, p in zip(row, prefix_sum[-1][1:])])
#     return prefix_sum


# def main():
#     # pylint: disable=unused-variable
#     R, C, Q = [int(x) for x in sys.stdin.readline().split()]
#     nums = [[int(x) for x in sys.stdin.readline().split()] for _ in range(R)]
#     prefix_sum = create_2d_prefix_sum(nums)
#     for _ in range(Q):
#         r1, c1, r2, c2 = [int(x) for x in sys.stdin.readline().split()]
#         pixel_sum = (prefix_sum[r2][c2] - prefix_sum[r1 - 1][c2] -
#                      prefix_sum[r2][c1 - 1] + prefix_sum[r1 - 1][c1 - 1])
#         size = (r2 - r1 + 1) * (c2 - c1 + 1)
#         print(pixel_sum // size)


# if __name__ == '__main__':
#     main()