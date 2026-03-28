x, y, w2, h2 = map(int, input().split())
w1, h1 = 0, 0

print(min(x-w1, w2-x, y-h1, h2-y))