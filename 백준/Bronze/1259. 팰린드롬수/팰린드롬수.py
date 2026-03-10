# sys.stdin.readline을 사용 시 개행문자('\n') 들어가니 해당 문장 지우세요!

while True:
    N = str(input())
    if N == '0':
        break
    elif N == N[::-1]:
        print('yes')
    else:
        print('no')