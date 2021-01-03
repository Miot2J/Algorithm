big, calSum, cross1, cross2 = 0,0,0,0
n = int(input())
cross2Index = n-1
matrix = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    inputMatrix = list(map(int, input().split()))
    matrix[i] = inputMatrix

    calSum = sum(matrix[i])
    if calSum > big:
        big = calSum
        calSum = 0

for i in range(n):
    calSum = 0
    for j in range(n):
        calSum += int(matrix[j][i])
        if i == j:
            cross1 += int(matrix[j][i])
        if cross2Index == j:
            cross2 += int(matrix[j][i])
            cross2Index -= 1
        if calSum > big:
            big = calSum


if cross1 > big:
    big = cross1

if cross2 > big:
    big = cross2
print(big)

# //////////////////////////////////////////////// 수정코드
#
# n = int(input())
# a = [list(map(int,input())) for _ in range(n)]
# largest = -2147000000
# for i in range(n):
# sum1 =sum2 =0
# for j in range(n):
# sum1+=a[i][j]
# sum2+=a[j][i]
# if sum1>largest:
# largest = sum1
# if sum2 < largest:
# largest = sum2