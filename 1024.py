
n, l = map(int, input().split())

for i in range(l, 101):
    start = max(n//i - i, 0)
    while True:
        sum1 = sum(range(start, start+i))
        if sum1 == n:
            for s in range(start, start+i):
                print(s, end=' ')
            exit(0)
        elif sum1 < n:
            start+=1
            continue
        else:
            break

print(-1)