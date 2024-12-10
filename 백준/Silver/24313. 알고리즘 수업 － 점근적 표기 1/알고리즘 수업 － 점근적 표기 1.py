import sys
input = sys.stdin.readline

a1, a = map(int, input().split())
c = int(input())
n0 = int(input())
if a1 <= c and a1 * n0 + a <= c * n0:
    print(1)
else:
    print(0)