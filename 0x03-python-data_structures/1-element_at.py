#!/usr/bin/python3

def element_at(my_list, idx):
    if (len(my_list) < idx < 0 or idx > len(my_list) or my_list is None):
        return None
    return my_list[idx]
