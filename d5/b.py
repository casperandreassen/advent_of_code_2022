import os
import re


stacks = [["B", "W", "N"], ["L", "Z","S", "P", "T", "D", "M", "B"], ["Q", "H", "Z", "W", "R"], ["W", "D", "V", "J", "Z", "R"], ["S", "H", "M", "B"], ["L", "G", "N", "J", "H", "V", "P", "B"], ["J", "Q", "Z", "F", "H", "D", "L", "S"], ["W", "S", "F", "J", "G", "Q", "B"], ["Z", "W", "M", "S", "C", "D", "J"]]

with open (os.getcwd() + "/d5/input.txt") as input:
    for i, line in enumerate(input):
        if i > 9:
            moves = re.findall(r'\d+', line.rstrip())
            tmp = stacks[int(moves[1]) - 1][len(stacks[int(moves[1]) - 1]) - int(moves[0]):len(stacks[int(moves[1]) - 1])]
            del stacks[int(moves[1]) - 1][len(stacks[int(moves[1]) - 1]) - int(moves[0]):len(stacks[int(moves[1]) - 1])]
            stacks[int(moves[2]) - 1].extend(tmp)
str = ""
for list in stacks:
    str += list.pop()

print(str)