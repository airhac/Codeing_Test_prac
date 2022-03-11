import sys
l = []
for i in range(9):

    l.append(int(sys.stdin.readline()))

def max(list):
    f = list[0]
    cnt =0
    for i in range(1,len(list)):
        if list[i] > f:
            f=list[i]
            cnt = i
    print(f)
    print(cnt+1)    

max(l)
#import sys
#l = []
#for i in range(9):
#    l.append(int(sys.stdin.readline()))
#
#print(max(l))
#print(l.index(max(l))+1)