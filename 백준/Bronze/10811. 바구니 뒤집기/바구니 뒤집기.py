# 리스트 슬라이싱 사용
N, M = map(int, input().split())
baskets = [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    i, j = i-1, j-1
    # i부터 j까지 역순으로 나타내기
    baskets[i:j+1] = reversed(baskets[i:j+1])
print(*baskets)

