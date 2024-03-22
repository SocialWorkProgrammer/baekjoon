H, M = map(int, input().split())
cook = int(input())

# 분 단위로 계산하면 됨
def cooking(H, M, cook):
    H = H * 60
    time = H + M
    time = time + cook
    return calc(time)

def calc(time):
    if time >= 1440:
        time = time - 1440
        hour = time // 60
        minute = time % 60
        return hour, minute
    else:
        hour = time // 60
        minute = time % 60
        return hour, minute

print(*cooking(H, M, cook))