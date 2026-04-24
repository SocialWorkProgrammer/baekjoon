def sizecom(wallet, fold): # 크기 비교 함수
    if max(wallet) >= max(fold) and min(wallet) >= min(fold):
        return True
    return False
            
def solution(wallet, bill):
    answer = 0
    while sizecom(wallet, bill) != True:
        if bill[0] > bill[1]:
            bill[0] //= 2
        else:
            bill[1] //= 2
        answer += 1
    return answer