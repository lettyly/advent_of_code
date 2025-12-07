ranges = []
searchKeys = []
freshIDs = 0

with open("2025/inputs/input5.txt") as file_in:
    for line in file_in:
        if line.find('-') >= 0:
            ranges.append(line.rstrip())
        elif len(line.rstrip()) > 0:
            searchKeys.append(int(line))

for key in searchKeys:
    for range in ranges:
        rangesSplit = range.split('-')
        if key >= int(rangesSplit[0]) and key <= int(rangesSplit[1]):
            freshIDs += 1
            break

print(freshIDs)
        
