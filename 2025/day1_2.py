import math

lines = []
start=50
zeroCounter=0
direction=''

with open("2025/inputs/input1.txt") as file_in:
    for line in file_in:
        lines.append(line)

for line in lines:
    direction=line[0]
    distance=line[1:]
    for _ in range(int(distance)):
        if direction == "R":
            start = (start + 1) % 100
        else: 
            start = (start - 1) % 100
        
        if start == 0:
            zeroCounter += 1

print('\n\nTotal count of zeroes')
print(zeroCounter) #5782
