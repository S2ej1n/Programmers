#한번에 한 유저 신고 가능. 한 유저 여러번 가능하나 동일하면 1회
#k번 이상 신고될시 게시판 이용 정지. -> 신고 유저에게 메일 보냄
#report : 이용자/신고당한자

def solution(id_list, report, k):
    #누가 누구를 신고했는지 저장하는 dic
    repor_dic = {}

    #신고당한 횟수를 저장하는 dic
    count_dic = {}
    #카운트를 위한 list
    count_list = []

    #결과 도출을 위한 list (신고 횟수 k 넘은 사람 담음)
    res_list = []

    #메일 받는 횟수를 저장하는 dic
    res_dic ={}

    #결과
    answer = []

    for i in range(len(report)):
        user = report[i].split(' ')[0]
        reped = report[i].split(' ')[1]

        #누가 누구를 신고했는지 저장
        if user not in repor_dic:
            repor_dic[user] = [reped]
        else:
            repor_dic[user] = list(set(repor_dic[user] + [reped]))

    #신고당한 횟수 저장
    for i in repor_dic: #우선 리스트에 담고
        count_list.append(repor_dic[i])

    for i in count_list: #리스트 순회
        for j in i:
            if j not in count_dic:
                count_dic[j] = 1
            else:
                count_dic[j] += 1

    #신고 횟수 k 이상인 유저 리스트에 담기
    for i in count_dic:
        if count_dic[i] >= k:
            res_list.append(i)

    for i in repor_dic:
        for j in range(len(res_list)):
            if res_list[j] in repor_dic[i]:
                if i not in res_dic:
                    res_dic[i] = 1
                else:
                    res_dic[i] += 1

    for i in id_list:
        if i in res_dic:
            answer.append(res_dic[i])
        else:
            answer.append(0)

    return answer