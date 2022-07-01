
direction = ['S','W','N','E']

now_x, now_y = 0,0
now_d = 0

array = [(now_x,now_y)]
n = int(input())
command = input()


for c in command:
    if c == 'R':
        now_d = (now_d+1)%4
    elif c == 'L':
        now_d = (now_d+3)%4
    elif c == 'F':
        if direction[now_d] == 'S':
            new = (now_x, now_y+1)
        elif direction[now_d] == 'W':
            new = (now_x-1, now_y)
        elif direction[now_d] == 'N':
            new = (now_x, now_y-1)
        elif direction[now_d] == 'E':
            new = (now_x+1, now_y)
        now_x, now_y = new
        array.append(new)

max_x, max_y = -9999,-9999
min_x, min_y = 9999,9999
for a in array:
    if max_x < a[0]:
        max_x = a[0]
    if max_y < a[1]:
        max_y = a[1]
    if min_x > a[0]:
        min_x = a[0]
    if min_y > a[1]:
        min_y = a[1]

for i in range(min_y, max_y+1):
    for j in range(min_x, max_x+1):
        # print((i,j))
        if (j,i) in array:
            print('.',end='')
        else:
            print('#',end='')
    print()
