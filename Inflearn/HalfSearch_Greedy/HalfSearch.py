n, m = input().split()
count = 0
numList = input().split()

numList.sort()
for i in numList:
    count += 1
    if i == m:
        print(count)
