from collections import Counter
def solution(a):
    answer = 0
    if len(a) <= 1:
        return 0
    dic = Counter(a).most_common()
    cnt = { k : v for k, v in dic}
    for n in cnt:
        if cnt[n] * 2 <= answer:
            continue
        count = 0
        i = 1
        while i < len(a):
            if (a[i] != n and a[i - 1] != n) or (a[i] == n and a[i - 1] == n):
                i += 1
                continue
            i += 2
            count += 2
        answer = max(answer, count)
    return answer
print(solution([ 1 , 2 , 1 , 3 , 2 , 4 , 3 , 5 , 6 , 7 , 3 , 8]))
