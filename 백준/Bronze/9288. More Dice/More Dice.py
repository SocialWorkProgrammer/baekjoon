import sys
input = sys.stdin.readline

X = int(input())
for tc in range(1,X+1):
    print(f"Case {tc}:")
    N = int(input())
    for i in range(1,7):
        for j in range(1,7):
            if i + j == N and i <= j:
                print(f"({i},{j})")
