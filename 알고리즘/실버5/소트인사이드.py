import sys
input = sys.stdin.readline
nums = list(input())
nums.sort(reverse=True)
print(''.join(nums))