#영어는 바꾸고, 숫자는 그대로 출력하고싶어..

import re

def solution(s):
    word = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6,
            'seven':7, 'eight':8, 'nine':9}

    keylist = list(word.keys())

    if s.isdigit() == True:
        answer = int(s)

    else:
        while True:
            isfound = False #있냐 없냐 재 검사 하는 기준

            for i in range(len(keylist)):
                isin = s.find(keylist[i])

                if isin >= 0:
                    s = s[0:isin] + str(i) + s[isin+1:]
                    isfound = True 

            if not isfound:
                break

    newS = re.sub(r"[^0-9]","",s)

    answer = int(newS)

    return answer