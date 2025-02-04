import sys
import math

# 1. 에라토스테네스의 체 + 소수 판별 알고리즘 이용 -> 시간초과
# def isprime(a):
#     if a < 2:
#         return False
#     if a == 2 or a == 3:
#         return True
#     for i in range(2, int(math.sqrt(a)+1)):
#         if a % i == 0:
#             return False
#     return True
#
# numlst = [x for x in range(1, 1000000)]
# for num in numlst:
#     if isprime(num):
#         numlst[2*num-1::num] = [0] * len(numlst[2*num-1::num])
# numset = set(filter(lambda x: x != 0, numlst[2::]))

# 에라토스테네스의 체 성능 개선
lst = [x for x in range(1000000)]
lst[0] = lst[1] = False
for i in range(2, int(math.sqrt(1000000)) + 1):
    if lst[i] != False:
        for j in range(i * i, 1000000, i):
            lst[j] = False
lst = set(filter(lambda x: x != False, lst))

T = int(input())
for tc in range(T):
    N = int(input())
    cnt = 0
    for i in range(1, N//2 + 1):
        if i in lst and N-i in lst:
            cnt += 1
    print(cnt)