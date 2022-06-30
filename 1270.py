
n = int(input())

for _ in range(n):
    array = list(map(int, input().split()))
    number = array.pop(0)
    array.sort()
    flag = 0

    cnt = 1
    for i in range(number-1):
        if array[i] == array[i+1]:
            cnt+=1
            if cnt > number/2:
                flag += 1
                print(array[i])
                break
        else:
            cnt = 1

    if flag == 0:
        print('SYJKGW')