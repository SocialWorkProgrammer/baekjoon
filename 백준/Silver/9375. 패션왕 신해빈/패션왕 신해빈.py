import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
for tc in range(N):
    clothes = defaultdict(int)
    for i in range(int(input())):
        cloth, kind = input().split()
        clothes[kind] += 1
    cnt = 1
    for j in clothes.values():
        cnt *= j + 1
    print(cnt - 1)
