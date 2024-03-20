from itertools import combinations

N = int(input())
taste = [list(map(int, input().split())) for _ in range(N)]
tastelst = []
# 시간 나면 재귀로도 풀어보자
for r in range(1, N+1):
    tastelst += list(combinations(taste, r))

sums = 0
result = []
while sums != len(tastelst):
    if len(tastelst[sums]) == 1:
        # 나중에 절댓값 잊지마!
        result.append(abs(tastelst[sums][0][1] - tastelst[sums][0][0]))
        sums += 1
    else:
        # tastelst 원소의 원소가 2개 이상일 때, for문으로 신맛끼리 곱하고, 쓴맛끼리 더하기
        sin, ssun = 1, 0
        for i in range(len(tastelst[sums])):
            sin *= tastelst[sums][i][0]
            ssun += tastelst[sums][i][1]
        result.append(abs(sin - ssun))
        sums += 1
print(min(result))