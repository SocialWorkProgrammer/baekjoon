import sys, math
input = sys.stdin.readline
def rounds(num):
    if num - int(num) >= 0.5:
        return math.ceil(num)
    else:
        return math.floor(num)

N = int(input())
if N == 0:
    print(0)
else:
    lst = sorted([int(input()) for i in range(N)])
    mins = rounds(N*0.15)
    lst = lst[mins:N-mins]
    print(rounds(sum(lst)/len(lst)))