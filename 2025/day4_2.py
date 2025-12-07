map=[]
rollsRemoved=0

with open("2025/inputs/input4.txt") as file_in:
    for line in file_in:
        map.append(list(line.rstrip()))

while True:
    rolls=0
    for row in range(len(map)):
        for col in range(len(map[row])):
            itemsAround=0
            if map[row][col] == '@':
                for chkRow in range (max(0, row-1), min(row+1, len(map)-1) + 1):
                    for chkCol in range (max(0, col-1), min(col+1, len(map[row])-1) + 1):

                        if map[chkRow][chkCol] == '@':
                            itemsAround += 1
                
                if itemsAround < 5:
                    map[row][col] = 'x'
                    rolls += 1
    if rolls == 0:
        break

    rollsRemoved += rolls

print((rollsRemoved))