lines=[]
maxPower=[]

with open("2025/inputs/input3.txt") as file_in:
    for line in file_in:
        lines.append(line)

for line in lines:
    firstNum = max(list(line[:-2]))
    index = line.find(firstNum)
    secondNum = max(list(line[index+1:]))
    maxPower.append(int(firstNum) * 10 + int(secondNum))

print(sum(maxPower))