import sys
# sys.stdin = open('input.txt','r')

T = int(input())
council = [list(map(int, sys.stdin.readline().split())) for _ in range(T)]

lst = [0 for i in range(T+1)]

for i in range(T):
    for j in range(i+council[i][0], T+1):
        if lst[j] < lst[i] + council[i][1]:
            lst[j] = lst[i] + council[i][1]

print(lst[-1])