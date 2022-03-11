for _ in range(int(input())):
	R1,R2 =input().split(' ')
	for j in list(R2):
		print(j*int(R1), end='')
	print()