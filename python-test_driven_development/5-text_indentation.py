#!/usr/bin/python3
"""
This is the "text_indentation" module.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    Args:
        text: a string

    Returns:
        print out the formatted string to console
    """
    t_msg = "text must be a string"
    m_msg = "text_indentation() missing 1 required positional argument: 'text'"
    if not isinstance(text, str):
        raise TypeError(t_msg)
    new_line = False
    for char in text:
        if new_line:
            if char == ' ':
                continue
            new_line = False
        if char =='.' or char == '?' or char == ':':
            print(char)
            print('')
            new_line = True
        else:
            print(char, end='')
