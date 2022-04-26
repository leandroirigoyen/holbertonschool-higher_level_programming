#!/usr/bin/python3
for number in range(0, 9):
    for number2 in range(0, 9):
        if number != number2:
            print(number, number2, end=', ')
