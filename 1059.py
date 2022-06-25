
# 본질적인 알고리즘은 쉬웠지만 조건이 꽤 까다로웠다.
# 0을 추가해서 1<=n<=max(S)의 조건을 걸어줘야하는 문제였다.

l = int(input())
array = list(map(int, input().split()))
n = int(input())

array.append(0)
array.sort()
left, right = 0,0

for i in range(len(array) - 1):
    if array[i] <= n <= array[i+1]:
        left, right = array[i], array[i+1]
        break

cnt = 0

for i in range(left+1, right):
    for j in range(i+1, right):
        if i<=n<=j:
            cnt+=1

print(cnt)