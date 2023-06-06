#!/usr/bin/python3
def print_last_digit(number):
    nbr = (number % 10, 10-number % 10)[number < 0]
    print(nbr)
    return nbr
