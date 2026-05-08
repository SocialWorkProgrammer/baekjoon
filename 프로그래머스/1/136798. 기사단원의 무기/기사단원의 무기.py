def divi(num): # 약수 구하기
    cnt = 0
    for i in range(1, int(num ** 0.5)+1):
        if num % i == 0:
            cnt += 1
            if i != num // i: # number//i가 i라면 제곱수가 되므로 제외. 서로 다르다면 cnt += 1(ex : num = 15, i = 3일 때 num//i = 5가 됨)
                cnt += 1
    return cnt

def solution(number, limit, power):
    answer = [1] # 원래 방식
    memo = {1:1}
    for num in range(2, number+1):
        memo[num] = divi(num)

    for num in range(2, number+1):
        if memo[num] > limit:
            answer.append(power)
        else:
            answer.append(memo[num])
    return sum(answer)
