def dice_counting(dice):
    cnt = 0
    for i in range(3):
        if dice[i] == dice[(i+1)%3]:
            cnt += 1
    return gambling(cnt)
    # return cnt

def gambling(cnt):
    if cnt == 0:
        return max(dice) * 100
    if cnt == 1:
        for i in range(1, 7):
            if dice.count(i) == 2:
                return dice[dice.index(i)] * 100 + 1000
    if cnt == 3:
        return  max(dice) * 1000 + 10000




dice = list(map(int, input().split()))
print(dice_counting(dice))