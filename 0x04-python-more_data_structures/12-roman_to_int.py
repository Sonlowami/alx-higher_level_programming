#!/usr/bin/python3
def roman_to_int(roman_string):
    # create a map of roman and numeric conversions
    dic_1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    # map roman symbol to their position in dic_1
    dic_2 = {'I': 0, 'V': 1, 'X': 2, 'L': 3, 'C': 4, 'D': 5, 'M': 6}
    # create a result list
    result = []
    new, first = '', ''
    count = i = 0
    is_before = False
    if type(roman_string) is str and roman_string is not None:
        while i < len(roman_string):
            first = roman_string[i]
            count += 1
            j = i + 1
            while j < len(roman_string):
                new = roman_string[j]
                if new == first:
                    count += 1
                    j += 1
                    continue
                elif dic_2[first] < dic_2[new]:
                    is_before = True
                    minus = dic_1[first]
                    count += 1
                    break
                break
            if is_before:
                result.append(dic_1[new] - minus)
            else:
                result.append(dic_1[first] * count)
            i += count
            count = 0
            is_before = False
        res = sum(result)
        return res
    return 0
