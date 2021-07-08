def DFS(x, y):
    global arr
    if x == 0 and y == 0:
        return arr[0][0]
    else:
        if y == 0:
            return DFS(x - 1, y) + arr[x][y]
        elif x == 0:
            return DFS(x, y - 1) + arr[x][y]
        else:
            return min(DFS(x - 1, y), DFS(x, y - 1))+arr[x][y]


if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dy = [[0] * n for _ in range(n)]
    print(DFS(n - 1, n - 1))
