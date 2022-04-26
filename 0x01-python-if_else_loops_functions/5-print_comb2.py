#!/usr/bin/python3
for number in range(0, 100):
    if number == 99:
        print(format(number, '02d'))
    else:
        print(format(number, '02d'), end=', ')
