T = int(input())
for tc in range(1, T+1):
    R, S = input().split()
    P = ''
    for i in range(len(S)):
        P += S[i] * int(R)
    print(P)