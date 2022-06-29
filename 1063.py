
king, stone, n = input().split()

n = int(n)
king_x = ord(king[0])
king_y = int(king[1])
stone_x = ord(stone[0])
stone_y = int(stone[1])

def next_pos(command, x, y):
    if command == 'R':
        return (x+1, y)
    elif command == 'L':
        return (x-1, y)
    elif command == 'B':
        return (x, y-1)
    elif command == 'T':
        return (x, y+1)
    elif command == 'RT':
        return (x+1, y+1)
    elif command == 'LT':
        return (x-1, y+1)
    elif command == 'RB':
        return (x+1, y-1)
    elif command == 'LB':
        return (x-1, y-1)
    else:
        return (x,y)

for _ in range(n):
    command = input()
    king_x_temp, king_y_temp = next_pos(command, king_x, king_y)
    stone_x_temp = stone_x
    stone_y_temp = stone_y
    if king_x_temp == stone_x and king_y_temp == stone_y:
        stone_x_temp, stone_y_temp = next_pos(command, stone_x, stone_y)

    if ord('A')<=king_x_temp<=ord('H') and ord('A')<=stone_x_temp<=ord('H') and 1<=king_y_temp<=8 and 1<=stone_y_temp<=8:
        king_x, king_y = king_x_temp, king_y_temp
        stone_x, stone_y = stone_x_temp, stone_y_temp

print(chr(king_x) + str(king_y))
print(chr(stone_x) + str(stone_y))