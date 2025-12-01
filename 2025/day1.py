import math

lines = []
start=50
zeroCounter=0

with open("input1.txt") as file_in:
    for line in file_in:
        lines.append(line)

for line in lines:
    number = line.replace('\n','')
    number = number.replace('R','-')
    number = number.replace('L','+')
    start += int(number)
    start = math.fmod(start, 100)
    if start==0:
        zeroCounter += 1

print('\n\nResult of zeroes')
print(zeroCounter)
print(start)
