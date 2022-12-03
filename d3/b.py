import os

# UPPERCASE - 38
# LOWERCASE - 96

score = 0

with open (os.getcwd() + "/d3/input.txt") as input:
    group = []
    for i, line in enumerate(input):
        group.append(line.rstrip())
        if (i + 1) % 3 == 0 and i != 0:
            for c in group[0]:
                if c in group[1] and c in group[2]:
                    if c.isupper():
                        score += ord(c) - 38
                        break
                    else:
                        score += ord(c) - 96
                        break
            group = []
print(score)