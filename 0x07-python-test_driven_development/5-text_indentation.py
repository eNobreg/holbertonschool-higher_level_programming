#!/usr/bin/python3
""" This Module  """


def text_indentation(text):
    """ Indents text at special characters  """
    rep_char = ['.', ':', '?']
    new_str = ""
    i = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    while i < len(text):
        if text[i] in rep_char:
            new_str += text[i]
            i += 1
            if i is not len(text):
                if (text[i] is ' '):
                    while text[i] == ' ':
                        i += 1 
            new_str += "\n\n"
            continue;
        new_str += text[i]
        i += 1
    print("{}".format(new_str), end='')
