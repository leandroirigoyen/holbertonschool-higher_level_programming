#!/usr/bin/python3
def element_at(my_list, idx):
    
    stlen = len(my_list)
    if idx > stlen:
        print("None")
    elif idx < 0:
        print("None")
    else:
        return my_list[idx]
    #if idx < 0:
        #print("None")
    #elif idx > len(my_list):
        #print("None")
        #print("{}".format(my_list[idx]))
