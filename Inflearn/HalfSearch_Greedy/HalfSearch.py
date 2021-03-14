n, m = map(int,input().split())
count = 0
numList = list(map(int, input().split()))

numList.sort()
lt = 0
rt = n-1

while lt <= rt:
    mid = (lt+rt)//2
    if numList[mid] == m:
        print(mid+1)
        break
    elif numList[mid] > m:
        rt = mid-1
    else:
        lt = mid +1
