import re
def solution(dartResult):
    answer = []
    scores = []
    numbers = [i for i in range(11)]
    s = dartResult[0]
    scores = re.findall('([0-9]+)([A-Z]+)(\W*)', dartResult)

    for score in scores:
        if score[1] == 'S':
            answer.append(int(score[0]))
            if score[2] != '':
                if score[2] == '*':
                    answer[-2:] = list(map(lambda x : x * 2, answer[-2:]))
                elif score[2] == '#':
                    answer[-1] *= -1
        elif score[1] == 'D':
            answer.append(int(score[0]) ** 2)
            if score[2] != '':
                if score[2] == '*':
                    answer[-2:] = list(map(lambda x : x * 2, answer[-2:]))
                elif score[2] == '#':
                    answer[-1] *= -1
        elif score[1] == 'T':
            answer.append(int(score[0]) ** 3)
            if score[2] != '':
                if score[2] == '*':
                    answer[-2:] = list(map(lambda x : x * 2, answer[-2:]))
                elif score[2] == '#':
                    answer[-1] *= -1

    return sum(answer)
print(solution('1D2S3T*'))
