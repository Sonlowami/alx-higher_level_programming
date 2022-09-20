#!/usr/bin/python3
for number in range(99):
    if (number % 16) < 10:
        if not ((number // 16) == 0):
            print(f"{number} = 0x{number // 16}{number % 16}")
        else:
            print(f"{number} = 0x{number % 16}")
    elif (number % 16) == 10:
        if not ((number // 16) == 0):
            print(f"{number} = 0x{number // 16}a")
        else:
            print(f"{number} = 0xa")
    elif (number % 16) == 11:
        if not ((number // 16) == 0):
            print(f"{number} = 0x{number // 16}b")
        else:
            print(f"{number} = 0xb")
    elif (number % 16) == 12:
        if not ((number // 16) == 0):
            print(f"{number} = 0x{number // 16}c")
        else:
            print(f"{number} = 0xc")
    elif (number % 16) == 13:
        if not ((number // 16) == 0):
            print(f"{number} = 0x{number // 16}d")
        else:
            print(f"{number} = 0xd")
    elif (number % 16) == 14:
        if not ((number // 16) == 0):
            print(f"{number} = 0x{number // 16}e")
        else:
            print(f"{number} = 0xe")
    elif (number % 16) == 15:
        if not ((number // 16) == 0):
            print(f"{number} = 0x{number // 16}f")
        else:
            print(f"{number} = 0xf")
