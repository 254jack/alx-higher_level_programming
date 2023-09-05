#!/usr/bin/python3
"""a text-indentation module."""


def text_indentation(text):
    """a function that print a text with two new lines after each '.', '?', and ':'.

    Args:
        text: text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    ch = 0
    while ch < len(text) and text[ch] == ' ':
        ch += 1

    while ch < len(text):
        print(text[ch], end="")
        if text[ch] == "\n" or text[ch] in ".?:":
            if text[ch] in ".?:":
                print("\n")
            ch += 1
            while ch < len(text) and text[ch] == ' ':
                ch += 1
            continue
        ch += 1
