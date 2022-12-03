import os

# UPPERCASE - 38
# LOWERCASE - 96

score = 0

with open (os.getcwd() + "/d3/input.txt") as input:
    for line in input:
        rucksack = line.rstrip()
        comp1 = rucksack[0: len(rucksack) // 2]
        comp2 = rucksack[len(rucksack) // 2: len(rucksack)]
        print(rucksack)
        print(comp1)
        print(comp2)
        for c in comp1:
            if c in comp2:
                if c.isupper():
                    score += ord(c) - 38
                    break
                else:
                    score += ord(c) - 96
                    break

print(score)