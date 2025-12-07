lines=[]
maxPower=[]

with open("2025/inputs/input3.txt") as file_in:
    for line in file_in:
        lines.append(line)

for line in lines:
    batteries=12
    maxnum=[]
    startIndex=0

    while batteries > 0:
        currentString=line[startIndex:len(line) - batteries]
        maxnum.append(max(list(currentString)))
        startIndex += currentString.find(maxnum[len(maxnum)-1]) + 1

        batteries -= 1

    maxPower.append(int(''.join(maxnum)))


print(sum(maxPower))
