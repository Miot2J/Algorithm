# 재귀 함수는 Stack 으로 쌓여 동작한다.
def DFS(x):
    if x > 0:
        DFS(x - 1)
        print(x)


if __name__ == "__main__":
    n = int(input())
    DFS(n)
