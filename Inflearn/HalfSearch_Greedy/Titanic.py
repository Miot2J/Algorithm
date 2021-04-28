from collections import deque

n, limit = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
# list -> deque 자료형으로 변환 deque는 자료 앞뒤로 넣고 빼기 가능(포인터 이동방식)
p = deque(p)
cnt = 0
while p:
    if len(p) == 1:
        cnt += 1
        break
    if p[0] + p[-1] > limit:
        p.pop()
        cnt += 1
    else:
        p.popleft()
        p.pop()
        cnt += 1
print(cnt)
