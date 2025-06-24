T = int(input())

for tc in range(T):
    temp = 0
    ans = 0
    test = list(map(str, input()))
    for te in test:
        if te != 'X':
            temp += 1
        else:
            temp = 0
        ans += temp
    print(ans)
