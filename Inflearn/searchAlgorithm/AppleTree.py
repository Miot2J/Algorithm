n = int(input())
numList = [list(map(int, input().split())) for _ in range(n)]
print(numList)
div = (n // 2)
addSum = 0
for i in range(n):
    absNum = abs(div - i)
    # print("abs = " + str(absNum))
    for k in range(0+absNum, n-absNum):
        # print(i,k)
        addSum += numList[i][k]
print(addSum)