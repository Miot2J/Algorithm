case, number = input().split()
# print('case='+ case, 'number ='+number)
list = input().split()
index = 0
sum = 0
count = 0
while(index < int(case)):
    sum += int(list[index])
    if int(list[index]) == int(number):
        count +=1
        sum = 0
    elif sum == int(number):
        count +=1
        sum = 0
        index -= 1
    index += 1

print(count)