N, M = map(int, input().split())

setlst = {input() for i in range(N)}
wordlst = [input() for tc in range(M)]

# 풀어쓴 코드
# cnt = 0
# for word in wordlst:
#     if word in setlst:
#        cnt += 1

# 컴프리헨션
print(sum(1 for word in wordlst if word in setlst))