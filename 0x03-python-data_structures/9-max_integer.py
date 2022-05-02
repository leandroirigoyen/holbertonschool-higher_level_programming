#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)

    maxinteger = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > maxinteger:
            maxinteger = my_list[i]

    return (maxinteger)
