N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for k in range(K):
    if A[k] < B[k]:
        A[k] , B[k] = B[k], A[k]
    else:
        break
    
print(sum(A))