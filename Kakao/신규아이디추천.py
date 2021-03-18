# https://programmers.co.kr/learn/courses/30/lessons/72410

import re
new_id = "abcdefghijklmn.p"

def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    print("1",new_id)
    # 2
    new_id = re.sub('[^a-z\d\-\_\.]','',new_id)
    print("2",new_id)
    # 3
    new_id = re.sub('\.\.+', '.',new_id)
    print("3",new_id)
    # 4
    new_id = re.sub('^\.|\.$', '',new_id)
    print("4",new_id)
    # 5
    if new_id == "":
        new_id = "a"
    print("5",new_id)
    # 6
    new_id = re.sub('\.$','',new_id[0:15])
    print("6",new_id)
    # 7
    answer = new_id
    if len(answer) <=2:
        addStr = answer[-1]
        while len(answer) <3:
            answer += addStr
    print(answer)
    return answer

solution(new_id)