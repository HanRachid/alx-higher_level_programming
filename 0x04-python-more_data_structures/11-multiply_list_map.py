#!/usr/bin/python3
def mutiply_list_map(my_list=[], number=0):
    if my_list is None:
        return None
    else:
        return my_list.map(lambda x: x*number, my_list)
