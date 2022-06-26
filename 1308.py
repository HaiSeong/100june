
def isLeap(year):
    if year % 400 ==0:
        return 1
    elif year % 100 == 0:
        return 0
    elif year % 4 == 0:
        return 1
    else:
        return 0

days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
leap_days = [0,31,29,31,30,31,30,31,31,30,31,30,31]

y1, m1, d1 = map(int ,input().split())
y2, m2, d2 = map(int ,input().split())


if y1 + 1000 < y2:
    print('gg')
    exit(0)
elif y1 + 1000 == y2:
    if m1 < m2:
        print('gg')
        exit(0)
    elif m1 == m2:
        if d1 <= d2:
            print('gg')
            exit(0)

cnt = 0
while True:
    if y1 == y2 and m1 == m2 and d1 == d2:
        break

    cnt += 1
    d1 += 1

    if isLeap(y1) == 0: # 평년
        if d1 > days[m1]:
            d1 = 1
            m1 += 1

        if m1 > 12:
            m1 = 1
            y1 += 1

    else: # 윤년
        if d1 > leap_days[m1]:
            d1 = 1
            m1 += 1

        if m1 > 12:
            m1 = 1
            y1 += 1

print('D-%d'%cnt)