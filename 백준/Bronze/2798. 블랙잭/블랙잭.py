from itertools import combinations


N, M = map(int, input().split())
cards = list(map(int, input().split()))
cardcombs = combinations(cards, 3)
closest_sum = 0
for cardcomb in cardcombs:
    current_sum = sum(cardcomb)
    if M >= current_sum and M-closest_sum >= M-current_sum:
        closest_sum = current_sum

print(closest_sum)