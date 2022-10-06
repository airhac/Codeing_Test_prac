from collections import defaultdict
import math
def solution(fees, records):
    answer = []
    parking = defaultdict(int)
    basic_time, basic_cost, cal_time, cal_cost = fees
    for record in records:
        time, number, case = record.split()
        time = int(time.split(':')[0]) * 60 + int(time.split(':')[1])
        if case == 'IN':
            parking[number] -= time
        else:
            parking[number] += time
    l = []
    for k in parking.keys():
        if parking[k] <= 0:
            l.append(k)
    for i in l:
        parking[i] += (23 * 60 + 59)
    #금액 정산하기
    car_num = sorted(parking.keys())
    for car in car_num:
        diff_time = parking[car] - basic_time
        tot_cost = basic_cost + (math.ceil(diff_time / cal_time) * cal_cost) if diff_time > 0 else basic_cost

        answer.append(tot_cost)
    return answer