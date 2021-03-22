n,m = map(int,input().split())
print(n,m)
array = [list( map(int, (input().split()))) for _ in range(m)]

print(array)
whole = 0
def recur(cloth):
    whole = 0
    whole += cloth
    return whole

recur(whole)
