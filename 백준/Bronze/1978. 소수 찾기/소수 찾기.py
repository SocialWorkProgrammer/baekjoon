N = int(input())
Nlst = list(map(int, input().split()))

result = 0

for num in Nlst: # 모든 원소를 하나씩 조사함
    cnt = 0
    if num > 1: # 1은 소수가 아니므로 패쓰
        for i in range(2, num): # 2부터 num까지
            if num % i == 0: # i로 나눴음에도 나머지가 있으면 cnt에 1 추가
                cnt += 1
        if cnt == 0: # 만약 다 했음에도 cnt가 0이라면
            result += 1 # 해당 num은 소수
print(result)
