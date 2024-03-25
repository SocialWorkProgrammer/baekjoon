import sys
# sys.stdin = open('input.txt','r')



total = 0
input = sys.stdin.readline
T = int(input())
result = ''
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    mx = arr[0]
    mx_start = mx_end = 0
    # tc 시작할 때마다 시작과 끝부분 모두 0으로 초기화
    start = end = 0
    # N번 반복
    for i in range(1, N):
        # 만약 arr[i]가 i-1과 i보다 더 크다면(?)
        if arr[i] >= arr[i-1] + arr[i]:
            # 시작, 끝부분 모두 i로 지정
            start = i
            end = i
        else:
            arr[i] = arr[i- 1] + arr[i]
            end = i
        # 만약 arr[i]가 mx보다 크다면
        if arr[i] > mx:
            # mx를 새로 지정
            mx = arr[i]
            mx_end = end
            mx_start = start
        elif arr[i] == mx and mx_end - mx_start > end - start:
            mx = arr[i]
            mx_end = end
            mx_start = start

    result += f'{mx_start + 1} {mx_end + 1}\n'
    total += mx

print(total)
print(result)
