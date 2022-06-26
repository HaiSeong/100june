
n = int(input())
cnt = 0

for i in range(n):
    visited = []
    string = input()
    is_group = True

    for i in range(len(string)):
        if i < len(string)-1  and string[i] == string[i+1]:
            continue
        if string[i] in visited:
            is_group = False
            break
        if string[i] not in visited:
            visited.append(string[i])

    if is_group:
        # print(string)
        cnt+=1

print(cnt)
