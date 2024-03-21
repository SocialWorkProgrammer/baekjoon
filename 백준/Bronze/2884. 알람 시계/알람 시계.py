H, M = map(int, input().split())

H = H * 60
time = H + M
time = time - 45
if time < 0:
    H = 23
    M = time % 60
else:
    H = time // 60
    M = time  % 60
print(H, M)