def solution(babbling):
    can_babbling = ["aya", "ye", "woo", "ma"]
    cannot_babbling = ["ayaaya", "yeye", "woowoo", "mama"] #이거 추가함...
    
    count = 0
    
    for b in babbling:
        for j in cannot_babbling:
            if j in b:
                b = b.replace(b,"Noo")
        
        for i in can_babbling:
            if i in b:
                b = b.replace(i," ") #그냥 ''라고 하면 다른 문자열과 합쳐지며 새로운 문자로 인식 가능
                                    #그래서 공백을 넣어줬다
        
        if b.isspace(): #문자가 모두 공백인지 확인
            count += 1
            
    return count