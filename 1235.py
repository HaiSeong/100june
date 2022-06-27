
n = int(input())
id = []
for _ in range(n):
    id.append(input())

id_len = len(id[0])

start = 1
end = id_len
m = 100

while start <= end:
    mid = (start+end)//2
    id_set = set()
    for i in id:
        id_set.add(i[-mid:])

    # print(start, mid, end)

    if len(id_set) == n:
        end = mid - 1
        m = mid
    else:
        start = mid + 1

print(m)