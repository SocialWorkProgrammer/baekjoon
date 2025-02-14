import sys
input = sys.stdin.readline

K = int(input())
stack = []
for tc in range(K):
    N = int(input())
    if N != 0:
        stack.append(N)
    if N == 0:
        stack.pop()
print(sum(stack))