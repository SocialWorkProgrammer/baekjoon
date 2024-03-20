import sys, heapq
N = int(input())
q = []

for i in range(N): # N번 반복(Nlst를 하나씩 뽑기 위함)
    Nlst = list(map(int, sys.stdin.readline().split())) # input보다 sys.stdin.readline()의 속도가 몇 배 더 빠르므로 애용할 것
    for j in range(N): # N번 반복(Nlst의 원소를 하나씩 heappush하기 위함)
        if len(q) < N: # q의 원소 개수가 N보다 적다면
            heapq.heappush(q, Nlst[j]) # 계속 추가해라
        if q[0] < Nlst[j]: # 그런데 q에서 가장 작은 원소보다 Nlst 원소가 더 작다면
            heapq.heappop(q) # q 첫째 원소를 없애고
            heapq.heappush(q, Nlst[j]) # 해당 Nlst 원소를 집어넣어라
print(q[0])





# 이 문제는 sort로 쉽게 풀릴줄 알았지만 시간 초과로 틀리게 된다
# heapq.heappush가 원소를 정렬하면서 넣어주기 때문에, 이를 이용해야 하므로 queue 문제라 할 수 있다.