import os

currentBiggestCarrier = 0

with open(os.getcwd() + "/d1/input.txt") as input:
    newCarrier = 0
    for line in input:
        if line.rstrip() == '':
            if newCarrier > currentBiggestCarrier:
                currentBiggestCarrier = newCarrier
                newCarrier = 0
            else:
                newCarrier = 0
        else:
            newCarrier += int(line.rstrip())

print(f'Biggest carrier carries {currentBiggestCarrier} calories')