N = int(input())
scores = list(map(int, input().split()))
lst = []
for i in range(N):
    lst.append(scores[i]/max(scores)*100)
print(sum(lst)/N)