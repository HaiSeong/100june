import math

def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))


t = int(input())
for _ in range(t):
    start_x, start_y, end_x, end_y = map(int, input().split())
    n = int(input())
    cnt = 0
    for _ in range(n):
        x,y,r = map(int, input().split())

        distance_to_start = distance(x, y, start_x, start_y)
        distance_to_end = distance(x, y, end_x, end_y)

        if distance_to_start < r and distance_to_end < r:
            pass
        elif distance_to_start < r or distance_to_end < r:
            cnt += 1
        else:
            pass

    print(cnt)