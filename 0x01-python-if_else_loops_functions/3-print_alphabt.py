#!/usr/bin/python3
for letter in range(97, 123):
    if not(letter == 101) and not(letter == 113):
        print(f"{chr(letter)}", end="")
