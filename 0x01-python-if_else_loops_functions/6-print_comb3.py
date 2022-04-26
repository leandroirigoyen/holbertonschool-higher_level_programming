#!/usr/bin/python3
for number in range(0, 9):
    for number2 in range(0, 10):
        if number2 > number:
            if number == 8 and number2 == 9:
                print(number, number2, sep='')
            else:
                print(number, number2, end=', ', sep='')
