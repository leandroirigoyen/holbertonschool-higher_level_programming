#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    new_tuple = tuple(map(lambda i, j: i+j, tuple_a, tuple_b))
    print(str(new_tuple)
