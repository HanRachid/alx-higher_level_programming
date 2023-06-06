#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if (i == 100):
            print("Buzz")
            continue
        if (i % 15 == 0):
            print("FizzBuzz ", end='')
            continue
        elif (i % 5 == 0):
            print("Buzz ", end='')
        elif (i % 3 == 0):
            print("Fuzz ", end='')
        else:
            print("{:d} ".format(i), end='')
