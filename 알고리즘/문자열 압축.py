def solution(s):
    result = []
    if len(s)==1:
        return 1
    for i in range(1, (len(s)//2) + 1):
        b = ''
        cnt = 1
        tmp = s[:i]
        for j in range(i,len(s),i):
            if tmp==s[j:j+i]:
                cnt+=1
            else:
                if cnt != 1:
                    b = b + str(cnt) + tmp
                else:
                    b = b + tmp
                tmp = s[j:j+i]
                cnt = 1
        if cnt != 1:
            b = b + str(cnt) + tmp
        else:
            b = b + tmp
        print(b)
        result.append(len(b))
    print(result)
    return min(result)

solution('aabbaccc')