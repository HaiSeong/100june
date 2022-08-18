n = int(input())
array = list(map(int, input().split()))

sorted_array = array[:]
sorted_array.sort()

visited = dict()
answers = []
cnt = 0

for a in sorted_array:
    if a not in visited:
        visited[a] = cnt
        cnt += 1
    else:
        pass

for a in array:
    print(visited[a], end=' ')