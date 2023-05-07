# L :(start *) 1,4,7 / R : (start #)3,6,9
# 가까운 손가락 : 2,5,8,0
# 둘 거리 같다면, 오른손잡이는 오른손, 왼손잡이는 왼손 씀.

def countdist(start,end):
    keypad_dic = {1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),
                  7:(2,0),8:(2,1),9:(2,2),"*":(3,0),0:(3,1),"#":(3,2)}
    start1 = keypad_dic[start][0]
    start2 = keypad_dic[start][1]
    end1 = keypad_dic[end][0]
    end2 = keypad_dic[end][1]

    return abs(start1 - end1) + abs(start2 - end2)

def solution(numbers, hand):
    #왼손 위치 저장
    left_loc = '*'; left_dist = 0
    #오른손 위치 저장
    right_loc = '#'; right_dist = 0

    res = []

    for num in numbers:
        if num == 1 or num == 4 or num == 7 :
            res.append('L')
            left_loc = num #왼손 위치 변경
        elif num == 3 or num == 6 or num == 9 :
            res.append('R')
            right_loc = num #오른손 위치 변경

        else: #가운데인 경우 2,5,8,0

            #left_dist = left_loc과 num의 거리 비교
            left_dist = countdist(left_loc,num)
            #right_dist = right_loc과 num의 거리 비교
            right_dist = countdist(right_loc,num)

            if left_dist == right_dist: #같을 경우
                if hand == "right":
                    res.append('R')
                    right_loc = num
                else: 
                    res.append('L')
                    left_loc = num
            elif left_dist > right_dist:
                res.append('R')
                right_loc = num
            else:
                res.append('L')
                left_loc = num

    answer = ''.join(res)
    return answer