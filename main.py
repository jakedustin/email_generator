import sys

with open('source.txt') as f:
    lines = f.readlines()

    for line in lines:
        print(line, end='')
