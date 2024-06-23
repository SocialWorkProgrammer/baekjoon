# 해결전략 : 큰 것부터 나눠 개수 구하기
for tc in range(int(input())):
    change = []
    money = int(input())
    for i in range(4):
        if i == 0:
            change.append(money // 25)
            money = money - 25 * change[0]
        elif i == 1:
            change.append(money // 10)
            money = money - 10 * change[1]
        elif i == 2:
            change.append(money // 5)
            money = money - 5 * change[2]
        elif i == 3:
            change.append(money)
    print(*change)