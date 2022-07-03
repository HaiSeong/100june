import math

def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

n = int(input())

for i in range(n):
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    x4, y4 = map(int, input().split())

    # ()/() * ()/() == -1
    if (y1-y3)*(y2-y4) == -1 * (x1-x3)*(x2-x4):
        if distance(x1,y1,x3,y3) == distance(x2,y2,x4,y4):
            print(1)
            continue
    elif (y1-y2)*(y3-y4) == -1 * (x1-x2)*(x3-x4):
        if distance(x1,y1,x2,y2) == distance(x3,y3,x4,y4):
            print(1)
            continue
    elif (y1-y4)*(y3-y2) == -1 * (x1-x4)*(x3-x2):
        if distance(x1,y1,x4,y4) == distance(x3,y3,x2,y2):
            print(1)
            continue
    print(0)