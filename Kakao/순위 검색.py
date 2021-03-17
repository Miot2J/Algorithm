# https://programmers.co.kr/learn/courses/30/lessons/72412?language=python3

query =["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]
info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]

def solution(info, query):
    count = 0
    answer = []
    info2 = []
    # 문자열 슬라이싱(점수 뽑기 위함)
    for infoArr in info:
        iLanguage, iPosition, iCareer, iSoulFood, iScore = infoArr.split()
        info2.append([iLanguage, iPosition, iCareer, iSoulFood, int(iScore)])
    # 점수로 소팅
    info2.sort(key = lambda num:num[-1])
    for queryArr in query:
        qLanguage, qAnd1, qPosition, qAnd2, qCareer, qAnd3, qSoulFood, qScore = queryArr.split()
        lt = 0
        rt = len(info2) - 1
        # 이분법으로 최소 점수컷 구간 구하기
        while lt <= rt:
            mid = (lt+rt)//2
            if info2[mid][-1] < int(qScore):
                lt = mid +1
            elif info2[mid][-1] >= int(qScore):
                if mid == 0 or info2[mid-1][-1] < int(qScore):

                    break
                else:
                    rt = mid-1
        for i in range(mid,len(info2)):
            iLanguage, iPosition, iCareer, iSoulFood, iScore = info2[i]
            if qLanguage != "-":
                if qLanguage != iLanguage:
                    continue
            if qPosition != "-":
                if qPosition != iPosition:
                    continue
            if qCareer != "-":
                if qCareer != iCareer:
                    continue
            if qSoulFood != "-":
                if qSoulFood != iSoulFood:
                    continue
            if int(qScore) <= int(iScore):
                count += 1

        answer.append(count)
        count = 0
    print(answer)
    return answer

solution(info,query)
