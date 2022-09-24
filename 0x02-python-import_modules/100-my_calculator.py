#!/usr/bin/python3
import calculator_1
import sys


def calculate(abc=[]):
    if abc[1] == '+':
        return calculator_1.add(int(abc[0]), int(abc[2]))
    elif abc[1] == '-':
        return calculator_1.sub(int(abc[0]), int(abc[2]))
    elif abc[1] == '*':
        return calculator_1.mul(int(abc[0]), int(abc[2]))
    elif abc[1] == '/':
        return calculator_1.div(int(abc[0]), int(abc[2]))


if __name__ == '__main__':
    arg = sys.argv
    if len(arg) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    ops = ['+', '-', '*', '/']
    if arg[2] not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print("{} {} {} = {}".format(arg[1], arg[2], arg[3], calculate(arg[1:4])))
