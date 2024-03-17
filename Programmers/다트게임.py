#3번의 기회 합 (0~10점)
#Single(S)-점수 1제곱, Double(D) - 2제곱, Triple(T) - 3제곱
#스타상(*) - 해당&바로 전 점수 각 2배, 첫 기회의 경우 스타상 점수만 두배, 중첩은 4배
#아차상(#) - 해당 점수 마이너스, 스타와 중첩 경우 -2
#점수|보너스|[옵션]

def solution(dartResult):

    #숫자 기준으로 잘라서 리스트 만들고, 그 리스트 안에서 영어랑 특수문자 분리.

    #한글자씩 자름
    letter = list(dartResult)
    newSection = []
    print(letter)

    for i in range(len(letter)):
        isNum = letter[i].isdigit() #숫자인지 판별

        if isNum == False:
            if letter[i] == 'S' :
                if letter[i-2].isdigit() == True: #10구분
                    cal = 10*1
                    newSection.append(cal)
                else:
                    cal = int(letter[i-1]) * 1
                    newSection.append(cal)

            elif letter[i] == 'D' :
                if letter[i-2].isdigit() == True: #10구분
                    cal = 10 * 10
                    newSection.append(cal)
                else:
                    cal = int(letter[i-1]) * int(letter[i-1])
                    newSection.append(cal)

            elif letter[i] == 'T' :
                if letter[i-2].isdigit() == True: #10구분
                    cal = 10*10*10
                    newSection.append(cal)
                else:
                    cal = int(letter[i-1]) * int(letter[i-1]) * int(letter[i-1])
                    newSection.append(cal)

            elif letter[i] == '*' :
                leng = len(newSection)
                #앞에 먼가 있을 경우
                if len(newSection) > 1 :
                    newSection[leng - 2] = newSection[leng - 2] * 2
                    newSection[leng - 1] = newSection[leng - 1] * 2
                #혼자 나온 경우
                else :
                    newSection[0] = newSection[0] * 2 

            elif letter[i] == '#' :
                leng = len(newSection)
                newSection[leng - 1] = newSection[leng - 1] * (-1)


    answer = newSection[0] + newSection[1] + newSection[2]
    return answer