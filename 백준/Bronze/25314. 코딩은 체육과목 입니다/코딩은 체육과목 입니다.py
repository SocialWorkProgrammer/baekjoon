ans = ''
## 재귀
# def recur(n):
#     global ans
#     if n == N:
#         return ans + 'int'
#     ans += 'long '
#     return recur(n+4)
#
# N = int(input())
# print(recur(0))

# 정석
N = int(input())
for i in range(N//4):
    ans += 'long '
ans += 'int'
print(ans)