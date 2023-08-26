#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0.0

    total_weight_sum = 0
    total_weight = 0

    for score, weight in my_list:
        total_weight_sum += score * weight
        total_weight += weight

    if total_weight == 0:
        return 0.0

    weight_avg = total_weight_sum / total_weight
    return weight_avg
