N, M = map(int, input().split())

setlst = {input() for i in range(N)}
wordlst = [input() for tc in range(M)]
cnt = 0
for word in wordlst:
    if word in setlst:
       cnt += 1

print(cnt)