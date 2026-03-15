import sys
from copy import deepcopy
input = sys.stdin.readline

N = int(input())
seq = [int(input()) for i in range(N)]
seqcopy = deepcopy(seq)
# print(f'seq = {seq}')


stack = [1] # 사용할 스택
seqstack = [] # 들어갈 스택

num = 2
ans = ['+']
for i in range(2 * N):
    if stack and stack[-1] == seq[0]:
        seqstack.append(stack.pop())
        seq.pop(0)
        ans.append('-')
    elif num <= N:
        stack.append(num)
        num += 1
        ans.append('+')
if seqcopy == seqstack:
    for i in ans:
        print(i)
else:
    print('NO')