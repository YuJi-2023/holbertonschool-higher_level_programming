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
    for char in ['.', '?', ':']:
        text = text.replace(char + ' ', char + '\n\n')
    print(text, end='')
