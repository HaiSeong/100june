# 정렬 문제

n = int(input())

strs = []
for _ in range(n):
    s = input()
    if s not in strs:
        strs.append(s)

strs.sort()
strs.sort(key=lambda x:len(x))

for s in strs:
    print(s)
