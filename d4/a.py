import os

inclusive = 0

with open (os.getcwd() + "/d4/input.txt") as input:
    elf1 = []
    elf2 = []

    for line in input:
        ranges = line.rstrip().replace(',',' ').replace('-',' ').split(' ')
        ranges = [int(x) for x in ranges]
        elf1 = ranges[0:2]
        elf2 = ranges[2:4]

        # Check if elf2 is contained in elf1
        if elf1[0] >= elf2[0] and elf1[1] <= elf2[1]:
            inclusive += 1
        # Check if elf1 is contained in elf2
        elif elf2[0] >= elf1[0] and elf2[1] <= elf1[1]:
            inclusive += 1

        elf1 = []
        elf2 = []

print(inclusive)