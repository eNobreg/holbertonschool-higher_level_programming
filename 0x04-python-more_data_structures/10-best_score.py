#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        for key, value in a_dictionary.items():
            return max(a_dictionary.keys())
    else:
        return None
