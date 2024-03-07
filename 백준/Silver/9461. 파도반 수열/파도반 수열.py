import sys

def trimemo(N):
    global memo
    if N >= len(memo):
        memo.append(trimemo(N-1) + trimemo(N-5))
    return memo[N]


T= int(sys.stdin.readline())
memo = [0, 1, 1, 1, 2, 2, 3, 4, 5]
for tc in range(1, T+1):
    N = int(sys.stdin.readline())
    if N < 9:
        print(memo[N])
    else:
        print(trimemo(N))

