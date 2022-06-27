
# 쉽게 풀었다. %연산을 잘 하면 바로 풀수 있었다.

n ,k = map(int, input().split())

i = 0

array = list(range(1,n+1))

print('<', end='')
while len(array)>1:
    i += k-1
    i%=len(array)
    print('%d, '%array[i], end='')
    array.remove(array[i])


print('%d'%array[0], end='')
print('>', end='')
