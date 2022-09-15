import re
def solution(files):
    answer = []
    arr = []
    store = {}
    for i, file in enumerate(files):
        store[i] = file
        temp = file.lower()
        part = re.search('([^0-9]+)([0-9]+)([^0-9]*)', temp)
        arr.append((part[1],int(part[2]), i))

    arr.sort()
    for _, _, index in arr:
        answer.append(store[index])
    return answer
#다른 사람풀이
#이분도 정규식을 가지고 풀었지만 저와 다르게 우선적으로 정렬을 해야하는것마다.
#정렬할떄 정규식을 lambda를 적요함으로써 코드를 줄였습니다.
#이러한식으로 lambda안에서도 정규식을 적용하여 바로 sort할 수 있다는것을 알수 있었습니다. 
import re

def solution(files):
    a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))
    b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
    return b