#!/usr/bin/python3
def uppercase(str):
    ptr = list(str)
    for i in range(len(str)):
        if (ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z')):
            ptr[i] = chr(ord(str[i])-32)
        if (i == len(str)-1):
            print(ptr[i])
            continue
        print("{:c}".format(ord(ptr[i])), end='')
