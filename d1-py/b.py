import os

currentBiggestCarriers = [0, 0, 0]

with open(os.getcwd() + "/d1-py/input.txt") as input:
    newCarrier = 0
    for line in input:
        if line.rstrip() == '':
            for i in range(3):
                if newCarrier > currentBiggestCarriers[i]:
                    if i < 2:
                        currentBiggestCarriers[i + 1] = currentBiggestCarriers[i]
                    currentBiggestCarriers[i] = newCarrier
                    newCarrier = 0
                    break
            newCarrier = 0
        else:
            newCarrier += int(line.rstrip())
print(currentBiggestCarriers)
print(f'Three biggest carriers carries {sum(currentBiggestCarriers)} calories')