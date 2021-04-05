 # 거스름돈을 걸러줄때 가장 작은 갯수의 동전이 되게한다.

n = 1260
count = 0
coin_types = [500,100,50,10]

for coin in coin_types:
    count += n //coin
    n %= coin
print(count)