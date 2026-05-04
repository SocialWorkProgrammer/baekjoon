from collections import deque
def solution(cards1, cards2, goal):
    # 큐 활용해서 하나씩 빼면서 goal에 맞춰가기
    cards1, cards2 = deque(cards1), deque(cards2)
    goal = deque(goal)
    for word in range(len(goal)):
        word1 = cards1[0] if cards1 else None
        word2 = cards2[0] if cards2 else None
        if goal[0] == word1:
                goal.popleft()
                cards1.popleft()
        elif goal[0] == word2:
                goal.popleft()
                cards2.popleft()
    if goal:
        return 'No'
    else:
        return 'Yes'
