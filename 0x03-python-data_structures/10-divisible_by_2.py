#!/usr/bin/python3
new_list = my_list[:]
    for i in range(len(new_list)):
        if new_list[i] % 2 == 0:
            new_list[i] = True
        else:
            new_list[i] = False
    return new_list
