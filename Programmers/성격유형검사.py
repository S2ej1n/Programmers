#1,7(매우) : 3 / 2,6 : 2 / 3,5(약간) : 1 / 4(모르겠음): 0
#더 높은 점수 / 같으면 사전순 빠른순.
#survey = 판단하는 지표 1차원 문자배열, choices = 선택지를 담은 정수 배열
#앞 : 비동의, 뒤 : 동의 

def solution(survey, choices):
    #지표
    per_list = ['RT','CF','JM','AN']
    #점수를 담은 딕셔너리
    score_dic = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}

    #결과 계산을 위한 딕셔너리
    res = {}

    #결과값 도출을 위한 리스트
    ans = []
    #사전순 비교 위한 리스트
    dic = []

    #딕셔너리에 값 추가
    for i in range(len(survey)):
        psn1 = survey[i][:1]
        psn2 = survey[i][1:]

        if choices[i]>=5 :
            if psn2 not in res:
                res[psn2] = score_dic[choices[i]]
            else:
                res[psn2] = res[psn2] + score_dic[choices[i]]
        elif choices[i] <= 3:
            if psn1 not in res:
                res[psn1] = score_dic[choices[i]]
            else:
                res[psn1] = res[psn1] + score_dic[choices[i]]
        else:
            pass
    print(res)

    #각 지표마다 비교하여 결과 도출.
    #1번 지표
    for i in range(len(per_list)):
        psn1 = per_list[i][:1]
        psn2 = per_list[i][1:]

        #성격유형이 딕셔너리에 있으면
        if psn1 in res:
            if psn2 in res: #뒤에것도 있으면 비교
                if res[psn1] > res[psn2]:
                    ans.append(psn1)
                elif res[psn1] < res[psn2]:
                    ans.append(psn2)
                else:
                    dic.append(psn1)
                    dic.append(psn2)
                    dic.sort()
                    ans.append(dic[0])
                    dic.clear()
            else: #뒤에거 없으면 그냥 앞에꺼 추가
                ans.append(psn1)
        else: #앞에꺼 없으면
            if psn2 in res:
                ans.append(psn2)
            else: #둘다 없으면
                dic.append(psn1)
                dic.append(psn2)
                dic.sort()
                ans.append(dic[0])
                dic.clear()

    answer = ''.join(ans)
    return answer