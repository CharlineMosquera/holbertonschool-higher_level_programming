#!/usr/bin/python3
"""function that prints a text"""

def text_indentation(text):
    """Prints the text with two new lines after
    each of the following characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        text = text.strip()
        punctuation = [".", "?", ":"]
        for char in text:
            print(char, end="")
            if char in punctuation:
                print("\n" * 2, end="")
