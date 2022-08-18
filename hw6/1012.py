from collections import deque
import sys

input = sys.stdin.readline

t = int(input())


def bfs(graph, visited, n, m, sy, sx):
    queue = deque([(sy, sx)])
    visited[sy][sx] = True
    graph[sy][sx] = 0

    while (queue):
        y, x = queue.popleft()
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny = dy + y
            nx = dx + x
            if 0 <= ny < n and 0 <= nx < m:
                if not visited[ny][nx]:
                    if graph[ny][nx] == 1:
                        graph[ny][nx] = 0
                        visited[ny][nx] = True
                        queue.append((ny, nx))


for _ in range(t):
    cnt = 0
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(graph, visited, n, m, i, j)
                cnt += 1
    print(cnt)