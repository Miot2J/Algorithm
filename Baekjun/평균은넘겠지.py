c = int(input())
for i in range(c):
    count = 0
    num_list = input()
    num_list = num_list.split()
    num_list = list(map(int, num_list))
    avg = sum(num_list[1:], 0.0) / num_list[0]
    for j in range(1, num_list[0] + 1):
        if num_list[j] > avg:
            count += 1
    print(format((count / num_list[0]) * 100, ".3f") + '%')
