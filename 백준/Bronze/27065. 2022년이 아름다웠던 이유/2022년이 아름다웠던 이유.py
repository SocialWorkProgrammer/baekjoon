import sys
input = sys.stdin.readline
from collections import defaultdict

memo = defaultdict(int)
memo2 = defaultdict(list)
for i in range(1, 5001):
    for j in range(1, i//2+1):
        if i/j == i//j:
            memo[i] += j
            memo2[i].append(j)

def discriminator(number):
    if memo[number] > number: # number가 과잉수
        cnt = 0
        for x in memo2[number]: # n을 제외한 모든 약수가 부족수이거나 완전수
            if memo[x] <= x:
                cnt += 1
        if cnt == len(memo2[number]):
            return 'Good Bye'
    return 'BOJ 2022'


T = int(input())
for tc in range(T):
    n = int(input())
    print(discriminator(n))
