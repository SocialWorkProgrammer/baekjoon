N, K = map(int, input().split())
wonlst = [int(input()) for i in range(N)]
cnt = 0
for i in wonlst[::-1]:
    cnt += K // i
    K = K % i
print(cnt)