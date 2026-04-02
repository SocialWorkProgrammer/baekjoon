import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
ans = [0] + [0 for i in range(N)] # 플레이어는 1번부터 시작하므로 기권 인덱스 0을 따로 추가

for i in lst:
    ans[i] += 1

# 표 많이 받은 한 명만 퇴출
if ans[1:].count(max(ans)) == 1:
    print(ans[1:].index(max(ans))+1) # 기권자 수가 더 많아도 표 많이 받은 사람이 한 명이면 퇴출되므로 리스트 슬라이싱 통해 기권자 수는 생략
else: # 표 많이 받은 사람이 없거나 두 명 이상일 경우 아무도 퇴출되지 않음
    print("skipped")