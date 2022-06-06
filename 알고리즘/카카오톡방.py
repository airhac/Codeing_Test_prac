def solution(record):
    answer = []
    id = {info.split()[1]: info.split()[2] for info in record if info.split()[0] != 'Leave'}
    for info in record:
        if info.split()[0] == 'Enter':
            answer.append(id[info.split()[1]] + '님이 들어왔습니다.')
        elif info.split()[0] == 'Leave':
            answer.append(id[info.split()[1]] + '님이 나갔습니다.')
    return answer