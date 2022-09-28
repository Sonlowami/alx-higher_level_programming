#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None and len(a_dictionary) > 0:
        best = list(a_dictionary.items())[0][0]
        for k, v in a_dictionary.items():
            if v > a_dictionary[best]:
                best = k
        return best
