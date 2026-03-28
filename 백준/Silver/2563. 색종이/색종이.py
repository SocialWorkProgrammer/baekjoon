N = int(input())
result = 0 # 색종이 넓이 총합
paper = [list(map(int, input().split())) for _ in range(N)]
papers = [[0 for i in range(101)] for j in range(101)]

for k, l in paper:
    for y in range(k, k+10):
        for x in range(l, l+10):
            papers[y][x] = 1
result = 0
for q in papers:
    result += q.count(1)
print(result)
