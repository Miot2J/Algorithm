
query =["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]
info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]

def solution(info, query):
    print(info)
    info.sort()
    print(info)
    sorted(info, key=lambda info: info[4])
    print(info)
    lt = 0
    rt = len(info) - 1
    count = 0
    answer = []
    for queryArr in query:
        qLanguage, qAnd1, qPosition, qAnd2, qCareer, qAnd3, qSoulFood, qScore = queryArr.split()
        for infoArr in info:
            iLanguage, iPosition, iCareer, iSoulFood, iScore = infoArr.split()
            print("qLanguage =" + qLanguage)
            if qLanguage != "-":
                print("if 1 qLanguage =" + qLanguage)
                if qLanguage != iLanguage:
                    print("if 2 qLanguage =" + qLanguage)
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
