#!/usr/bin/python3
import sys

def main(filename):
    file_lines = load(filename)
    line_lst = sort_lines(file_lines)
    print(file_lines)

def load(file):
    with open(file, 'r') as f:
        file_data = f.read()
        lines = file_data.splitlines()
        
    return lines

def sort_lines(file_lines):
    file_lines = sorted(file_lines, key=lambda el: int(el.split(' ')[0]))
    return file_lines

if __name__ == "__main__":
    main(sys.argv[1])