import sys
N = int(input())
lst = list(map(int, input().split()))

cnt = 1
stack = []
for i in lst:
    stack.append(i)
    while stack and stack[-1] == cnt:
        stack.pop()
        cnt += 1

print('Nice' if not stack else 'Sad')