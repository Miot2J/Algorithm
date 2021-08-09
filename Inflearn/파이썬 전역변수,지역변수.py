def DFS1():
    # 선언시 cnt가 지역변수로 동작함
    cnt = 3
    print(cnt)
def DFS2():
    # 비선언시 cnt가 전역변수로 동작함
    if cnt == 5:
        print(cnt)

if __name__ == "__main__":
    cnt =5
    DFS1()
    DFS2()
    print(cnt)