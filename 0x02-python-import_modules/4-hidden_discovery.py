#!/usr/bin/python3
import hidden_4 as h
if __name__ == "__main__":
    for i in dir(h):
        if (i[0] != '_' or i[1] != '_'):
            print(i)
