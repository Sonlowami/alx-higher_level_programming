#!/usr/bin/python3
i = 1
for x in range(9):
    for n in range(i, 10):
        if not (x * 10 + n == 89):
            print(f"{x}{n}", end=', ')
        else:
            print(f"{x}{n}")
    i += 1
