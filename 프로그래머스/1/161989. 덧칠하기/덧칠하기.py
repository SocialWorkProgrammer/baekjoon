def solution(n,m,section):
    # 모든 벽을 나타내는 리스트
    paintlst = [1 for i in range(n)]
    # 칠할 벽에 0 부여
    for sec in section:
        paintlst[sec-1] = 0
    cnt = 0 # 칠한 횟수
    for i in range(n):
        if paintlst[i] == 0: # 만약 벽이 칠해져있지 않다면, 연속된 구역만큼 색칠
            for j in range(i,i+m):
                if j > n - 1: # 만약 칠할 부분이 인덱스를 넘어간다면 break
                    break
                paintlst[j] += 1
            cnt += 1
    answer = cnt
    return answer
