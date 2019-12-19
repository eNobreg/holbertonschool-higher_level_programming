#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0


    if type(roman_string) is str:
        for i in range(len(roman_string)):
            if i > 0 and rom_dict[roman_string[i]] > rom_dict[roman_string[i - 1]]:
                num += rom_dict[roman_string[i]] - 2 * rom_dict[roman_string[i - 1]]
            else:
                num += rom_dict[roman_string[i]]
        return num
    return 0 
