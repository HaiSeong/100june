# 나누기에서 0이 나올 수 있는 수식은 항을 넘겨서 곱하기로 계산하자는 교훈을 얻었다.

import math

def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

def find_d(x1,y1,x2,y2,x3,y3):
    x4 = x1 + x3 - x2
    y4 = y1 + y3 - y2

    return (x4,y4)

def sum_distance(x1,y1,x2,y2,x3,y3,x4,y4):
    d1 = distance(x1,y1,x2,y2)
    d2 = distance(x2,y2,x3,y3)
    d3 = distance(x3,y3,x4,y4)
    d4 = distance(x4,y4,x1,y1)

    return d1+d2+d3+d4

x1,y1,x2,y2,x3,y3 = map(int, input().split())

if (x1==x2 and y1==y2) or (x1==x3 and y1==y3) or (x3==x2 and y3==y2):
    print(-1)
    exit(0)

if (y1-y2)*(x1-x3) == (y1-y3)*(x1-x2):
    print(-1)
    exit(0)

case1 = find_d(x1,y1,x2,y2,x3,y3)
case2 = find_d(x2,y2,x1,y1,x3,y3)
case3 = find_d(x1,y1,x3,y3,x2,y2)



sum1 = sum_distance(x1,y1,x2,y2,x3,y3,case1[0],case1[1])
sum2 = sum_distance(x2,y2,x1,y1,x3,y3,case2[0],case2[1])
sum3 = sum_distance(x1,y1,x3,y3,x2,y2,case3[0],case3[1])

print(max(sum1,sum2,sum3) - min(sum1,sum2,sum3))