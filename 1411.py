
n = int(input())

str = []
for _ in range(n):
    str.append(input())

cnt = 0

for index1 in range(n):
    for index2 in range(index1+1,n):
        str1 = str[index1]
        str2 = str[index2]
        flag = 1
        for i1 in range(len(str1)):
            for i2 in range(i1+1, len(str1)):
                if str1[i1] == str1[i2]:
                    if str2[i1] != str2[i2]:
                        flag = 0
                else:
                    if str2[i1] == str2[i2]:
                        flag = 0

        if flag == 1:
            cnt+=1

print(cnt)