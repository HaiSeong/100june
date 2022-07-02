
n = int(input())
array = []
for _ in range(n):
    array.append(input())

def sum_of_numbers(str):
    sum = 0
    for s in str:
        if '0'<=s<='9':
            sum += (ord(s)-ord('0'))

    return sum

array.sort()
array.sort(key=sum_of_numbers)
array.sort(key=lambda str:len(str))

for a in array:
    print(a)