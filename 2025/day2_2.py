import re

funnyNums=[]

with open("2025/inputs/input2.txt") as file_in:
    output = file_in.read().split(',')

for area in output:
    ranges = area.split('-')

    for val in range(int(ranges[0]), int(ranges[1])):
        pos = re.search(r"^(.+)(\1+)$", str(val))
        if pos is not None:
            funnyNums.append(val)

print(sum(funnyNums))