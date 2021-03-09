k, n = map(int, input().split())

intList = []
count, j = 0, 0
for _ in range(int(k)):
    intList.append(input())

temp = intList[1]
# 나누는 수 구하기
while True:
    j += 1
    div = int(intList[0]) // j

    # print(div)

    # 나눠서 카운터 더하기 코드
    for i in range(int(k)):
        # print("i", i , intList[i])
        count += int(intList[i]) // div
    if int(count) >= n:
        print(count)
        break
    count = 0

#4 11
#802
#743
#457 539



