import os

overlap = 0

with open (os.getcwd() + "/d4/input.txt") as input:
    elf1 = []
    elf2 = []

    for line in input:
        ranges = line.rstrip().replace(',',' ').replace('-',' ').split(' ')
        ranges = [int(x) for x in ranges]
        elf1 = ranges[0:2]
        elf2 = ranges[2:4]

        # inclusive test (StartA <= EndB) and (EndA >= StartB)
        if elf1[0] <= elf2[1] and elf1[1] >= elf2[0]:
            overlap += 1

        elf1 = []
        elf2 = []

print(overlap)