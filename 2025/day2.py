text = ''
funnyNums=[]

with open("2025/inputs/input2.txt") as file_in:
    output = file_in.read().split(',')

for area in output:
    ranges = area.split('-')

    for val in range(int(ranges[0]), int(ranges[1])):
        currentNum=str(val)
        if currentNum[:len(currentNum)//2] == currentNum[len(currentNum)//2:]:
            funnyNums.append(val)

print(sum(funnyNums))