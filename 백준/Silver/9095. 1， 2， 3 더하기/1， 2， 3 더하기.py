import sys
input = sys.stdin.readline



for tc in range(int(input())):
    memodict = {1: 1, 2: 2, 3: 4}
    N = int(input())
    def dp(x):
        if x in memodict.keys():
            return memodict[x]
        else:
            memodict[x] = dp(x-1) + dp(x-2) + dp(x-3)
        return memodict[x]
    print(dp(N))