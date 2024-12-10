import sys
input = sys.stdin.readline

n = int(input())
cnt = n * (n-1) * (n-2) / 6
print(int(cnt))
print(3)