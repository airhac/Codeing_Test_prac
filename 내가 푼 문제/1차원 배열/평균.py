N =  int(input())
input = list(map(int, input().split()))
max  = max(input)
mean_in = [(i/max)*100 for i in input]
print(sum(mean_in)/N)
