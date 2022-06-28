
n = int(input())
array = []
for _ in range(n):
    array.append(input())

max_cnt = -1
for i in range(n):
    first = array[i][:]
    second = ""
    for _ in range(n):
        second+='N'
    for f in range(n):
        if first[f] == 'Y':
            for j in range(n):
                if array[f][j] == 'Y':
                    second = second[:j] + 'Y' + second[j+1:]
                    #
                    # second[j] = 'Y'

    for j in range(n):
        if second[j] == 'Y':
            first = first[:j] + 'Y' + first[j+1:]
            # first[j] = 'Y'


    first = first[:i] + 'N' + first[i + 1:]
    # first[i] = 'N'

    cnt =0
    for j in range(n):
        if first[j] == 'Y':
            cnt+=1

    max_cnt = max(max_cnt, cnt)

print(max_cnt)