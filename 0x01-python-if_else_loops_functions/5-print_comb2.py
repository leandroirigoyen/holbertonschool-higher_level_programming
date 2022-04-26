#!/usr/bin/python3
for number in range(0, 100):
    if number!=number[-1]:
        print(format(number, '02d'), end=', ')
