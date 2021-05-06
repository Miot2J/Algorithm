n = int(input())
p = dict()

for i in range(n):
    p[input()] = 1
for i in range(n - 1):
    p[input()] = 0
for key, value in p.items():
    if value == 1:
        print(key)
        break