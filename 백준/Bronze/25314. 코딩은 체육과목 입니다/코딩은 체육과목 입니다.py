ans = ''
def recur(n):
    global ans
    if n == N:
        return ans + 'int'
    ans += 'long '
    return recur(n+4)

N = int(input())
print(recur(0))