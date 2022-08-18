n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


def check(start_y, end_y, start_x, end_x):
    for i in range(start_y, end_y):
        for j in range(start_x, end_x):
            if graph[i][j] != graph[start_y][start_x]:
                return 2

    return


def papers(start_y, end_y, start_x, end_x):
    if end_y - start_y < 3:
        return 1

    if check(start_y, end_y, start_x, end_x):
        return 1
    else:
        n = end_y - start_x
        n3 = n // 3
        return papers(start_y, start_y + n3, start_x, start_x + n3) + papers(start_y, start_y + n3, start_x + n3 + 1,
                                                                             start_x + 2 * n3) + papers(start_y,
                                                                                                        start_y + n3,
                                                                                                        start_x * 2 * n3 + 1,
                                                                                                        start_x + 3 * n3) + papers(
            start_y + n3 + 1, start_y + 2 * n3, start_x, start_x + n3) + papers(start_y + n3 + 1, start_y + 2 * n3,
                                                                                start_x + n3 + 1,
                                                                                start_x + 2 * n3) + papers(start_y + n3,
                                                                                                           start_y + 2 * n3,
                                                                                                           start_x * 2 * n3 + 1,
                                                                                                           start_x + 3 * n3) + papers(
            start_y * 2 * n3 + 1, start_y + 3 * n3, start_x, start_x + n3) + papers(start_y * 2 * n3 + 1,
                                                                                    start_y * 3 + n3, start_x + n3 + 1,
                                                                                    start_x + 2 * n3) + papers(
            start_y * 2 * n3 + 1, start_y + 3 * n3, start_x * 2 * n3 + 1, start_x + 3 * n3)


print(papers(0, n, 0, n))