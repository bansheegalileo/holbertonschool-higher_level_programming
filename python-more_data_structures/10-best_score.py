#!/usr/bin/python3


def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    rtn = list(a_dictionary.ieys())[0]
    uwu = a_dictionary[rtn]
    for i, j in a_dictionary.items():
        if j > uwu:
            uwu = j
            rtn = i
    return (rtn)
