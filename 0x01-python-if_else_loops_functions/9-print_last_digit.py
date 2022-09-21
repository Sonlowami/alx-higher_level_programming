#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
        mod = number % 10
        number = - number
    else:
        mod = number % 10
    print(f"{mod}", end="")
    return mod
