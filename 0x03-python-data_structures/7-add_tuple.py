#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a = 0
    b = 0

    i = len(tuple_a)-1
    j = len(tuple_b)-1

    while (i > 1 or j > 1):
        i -= 1
        j -= 1

    while (i > j):
        if i == 1:
            b = tuple_a[i]
        if i == 0:
            a = tuple_a[i]
        i -= 1
    while (j > i):
        if j == 1:
            b = tuple_a[i]
        if j == 0:
            a = tuple_a[i]
        j -= 1
    while (i >= 0):
        if i == 1:
            b = tuple_a[i] + tuple_b[i]
        if i == 0:
            a = tuple_a[i] + tuple_b[i]
        j -= 1
        i -= 1
    return (a, b)
