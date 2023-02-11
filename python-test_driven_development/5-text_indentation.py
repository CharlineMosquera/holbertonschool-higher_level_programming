#!/usr/bin/python3
"""function that prints a text"""


def text_indentation(text):
    """Prints the text with two new lines after
    each of the following characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        prev = 0
        punctuation = [".", "?", ":"]
        for i in range(len(text)):
            if i == len(text) - 1:
                print(text[prev:i + 1], end="")
            elif text[i] in punctuation:
                print(text[prev:i + 1], end="")
                print('\n')
                prev = i + 1
                while text[prev] == " ":
                    prev += 1
