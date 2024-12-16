N, M = map(int, input().split())
board = []
result = []
for tc in range(N):
    board.append(input())

for i in range(N-7):
    for j in range(M-7):
        board1 = 0
        board2 = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a + b) % 2 == 0:
                    if board[a][b] != 'W':
                        board1 += 1
                    elif board[a][b] != 'B':
                        board2 += 1
                else:
                    if board[a][b] != 'B':
                        board1 += 1
                    elif board[a][b] != 'W':
                        board2 += 1
        result.append(board1)
        result.append(board2)
print(min(result))