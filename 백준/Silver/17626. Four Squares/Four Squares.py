import sys
input = sys.stdin.readline
from math import isqrt

# 파이썬으로는 DP가 풀리지 않아 라그랑주 판별식 사용했습니다.
N = int(input())
def ragrange(x):
    if isqrt(x) ** 2 == x:
        return 1
    else:
        for i in range(1, isqrt(x)+1):
            remain = x - i ** 2
            if isqrt(remain) ** 2 == remain:
                return 2
        while x % 4 == 0:
            x //= 4
        if x % 8 == 7:
            return 4
        else:
            return 3
print(ragrange(N))