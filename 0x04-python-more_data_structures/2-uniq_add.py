#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_ints = set()
    total = 0

    for num in my_list:
        if isinstance(num, int) and num not in uniq_ints:
            total = total + num
            uniq_ints.add(num)
    return total
