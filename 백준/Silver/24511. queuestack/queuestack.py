import sys

input = sys.stdin.readline
from collections import deque

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int,input().split()))

queuestack = deque()
# 스택의 경우, LIFO이므로 들어간 수 그대로 나오기 때문에 큐의 경우만 넣으면 됨
for i in range(N):
    if A[i] == 0:
        queuestack.append(B[i])

for j in range(M):
    queuestack.appendleft(C[j])
    print(queuestack.pop(), end = ' ')