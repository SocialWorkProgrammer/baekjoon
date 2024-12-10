import sys
input = sys.stdin.readline

n = int(input())
# sum = 0
# for i in range(1, n-1):
#     sum += i * (i+1) / 2
sum = n * (n-1) * (n-2) / 6
print(int(sum))
print(3)