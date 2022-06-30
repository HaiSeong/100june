
n = int(input())
array = []
for _ in range(n):
    a, b = map(int, input().split())
    array.append(a-b)

array.sort()

if n % 2 == 0:
    print(1 + abs(array[n//2 - 1] - array[n//2]))
else:
    print(1)