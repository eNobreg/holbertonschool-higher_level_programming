#!/usr/bin/python3


def weight_average(my_list=[]):
    weight = 0
    result = []
    if len(my_list) is 0:
        return 0
    for i in my_list:
        weight += i[1]
        result.append(i[0] * i[1])
    return sum(result) / weight
