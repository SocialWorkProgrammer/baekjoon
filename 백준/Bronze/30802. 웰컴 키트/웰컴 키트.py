N = int(input())
shirts = list(map(int, input().split()))
T, P = map(int, input().split())
cnt = 0
for i in shirts:
    if i > 0:
        if i // T == 0:
            cnt += 1
        else:
            cnt += i // T
            if i % T > 0:
                cnt += 1
print(cnt)
print(N//P, N%P)