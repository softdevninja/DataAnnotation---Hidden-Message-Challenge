#!/usr/bin/python3
# *_* coding: utf-8 *_*

"""
A text file containing a hidden message will be passed as part of a system argument when running the script. If the lines within that file are not sorted, then
the method sort_lines will sort them. At the end a hidden message will be revealed. 
"""
__version__ = "1.0.0"
__author__ = "Doug Zuniga"
__email__ = "softdevninja@gmail.com"

import sys

def main(filename):
    """
    Script will load the file and store the line in a sorted manner in a list for the purpose of displaying a hidden message.

    Args:
        filename (object): Represents a text file type that is passed as a system argument when the script is ran. 
    """
    file_lines = load(filename)
    line_lst = sort_lines(file_lines)
    print(file_lines)

def load(file):
    """
    Opens the file and split each lines within that file.  Store all individual line as a string representation in a list

    Args:
        file (object): Represents the text file type that was passed over as an argument containing a hidden message. 

    Returns:
        list: Contains string representation of all the lines read from the text file that was opened. 
    """
    with open(file, 'r') as f:
        file_data = f.read()
        lines = file_data.splitlines()
        
    return lines

def sort_lines(file_lines):
    """
    Receives a list of string characters containing both a value as a number type string that is used for sorting purposes in the case the list is unsorted. 

    Args:
        file_lines (list): Represents a list containing individual lines that was read previously as a string of characters. 

    Returns:
        list: Sorted list of lines by numerical value in descending order.
    """
    file_lines = sorted(file_lines, key=lambda el: int(el.split(' ')[0]))
    return file_lines

if __name__ == "__main__":
    main(sys.argv[1])