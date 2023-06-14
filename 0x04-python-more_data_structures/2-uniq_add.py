#!/usr/bin/python3
def uniq_add(my_list=[]):
    already = []
    sum = 0
    for i in my_list:
        if i in already:
            continue
        already.append(i)
        sum += i
    return sum
