a = input()
b = input()
stringHash = dict()

for x in a:
    stringHash[x] = stringHash.get(x, 0) + 1
for x in b:
    stringHash[x] = stringHash.get(x, 0) - 1

for x in a:
    if stringHash.get(x) != 0:
        print("NO")
        break
else:
    print("YES")

