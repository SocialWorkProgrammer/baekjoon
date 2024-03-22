T = int(input())
for tc in range(1, T+1):
    ans = ' ' * (T-tc) + '*' * tc
    print(ans)