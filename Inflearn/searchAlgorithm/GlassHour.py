n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
print(matrix)
m = int(input())
for _ in range(m):
    row, direction, number = map(int,input().split())
    if direction == 0:
        for _ in range(number):
            tmp = matrix[row-1].pop(0)
            print(tmp)
            matrix[row-1].append(tmp)
    elif direction == 1:
        for _ in range(number):
            tmp = matrix[row-1].pop()
            matrix[row-1].insert(0,tmp)
div = n // 2
numSum, start, end = 0, 0, n
for i in range(n):
    for num in range(start, end):
        numSum += matrix[i][num]
    if i < div:
        start += 1
        end -= 1
    else:
        start -= 1
        end += 1

for i in matrix:
    print(i)

print("numSum = ", numSum)