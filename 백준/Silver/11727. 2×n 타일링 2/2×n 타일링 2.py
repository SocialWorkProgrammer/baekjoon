N = int(input())
DP = [0,1,3] # n과 헷갈리지 않도록 맨 앞에 0추가, n=1,2일 경우도 추가
for i in range(N+1):
    if i >= 3: # i가 3 이상이어야 DP 리스트가 깨지지 않음
        DP.append(DP[i-1] + 2 * DP[i-2])
print(DP[N]%10007)
