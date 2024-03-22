N = int(input()) # 카드 묶음 개수
arr = [int(input()) for _ in range(N)]
# 히든테케가 정렬되어 있을 것이라는 보장이 읎다.
card_sum = 0

# 큐를 통해 두개씩 더한 후 빼고, 더해진 것을 가장 뒤에 붙여 리스트가 빌 때까지 반복
from heapq import heappush, heappop

lst = []
arr.sort()
# start = time.time()
while arr:
    if len(arr) == 1:
        print(card_sum)
        break
    else:
        a = heappop(arr)
        b = heappop(arr)
        heappush(arr, a + b)
        card_sum += a + b
