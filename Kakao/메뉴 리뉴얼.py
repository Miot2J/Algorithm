
# 주어진 문자열에서 조합을 구하고 (combination 사용) 튜플형태의 리턴값을 리스트로 변경 후 문자열을 합쳐줌
# ex) ('A','C') -> ['AC']
# 더블 리스트 형태의 문자열의 값을 Key 값으로 딕셔너리에 저장
# 딕셔너리 Key를 기반으로 Value 업데이트
# course 조건의 숫자와 길이가 같은 key의 Value중 가장 높은 값(biggestNum)들을 저장
# 딕셔너리 순회하며 biggestNum과 매칭하여 key값 answer 리스트에 저장 후 리턴


from itertools import combinations

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]

def solution(orders, course):
    answer = []
    biggestKey = []
    dict = {}
    for orderItems in orders:
        orderList = list(orderItems)
        orderList.sort()
        for i in course:
            dictionKey = list(combinations(orderList, i))
            if dictionKey != []:
                for j in range(len(dictionKey)):
                    dictionKey[j] = list(dictionKey[j])
                    dictionKey[j] = ''.join(dictionKey[j])

            for key in dictionKey:
                if key in dict:
                    dict[key] =dict[key]+ 1
                else:
                    dict[key] = 1
    for i in course:
        biggestNum = 0
        for key in dict:
            if len(key) == i:
                if dict[key] >= biggestNum:
                    biggestNum = dict[key]
                    # print(key,biggestNum)
        for key in dict:
            if len(key) == i:
                if dict[key] == biggestNum and biggestNum > 1:
                    answer.append(key)
    answer.sort()
    print(answer)
    return answer

solution(orders,course)