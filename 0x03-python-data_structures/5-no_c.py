#!/usr/bin/python3
def no_c(my_string):
    #s = my_string
    #''.join(c for c in s if c not in 'Cc')
    print(my_string.translate({ord(i): None for i in 'Cc'}))
