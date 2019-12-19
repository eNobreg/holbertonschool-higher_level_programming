#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0


    if type(roman_string) is str:
        for i in range(len(roman_string)):
            num += rom_dict[roman_string[i]]
        return num
    else:
        return 0 
