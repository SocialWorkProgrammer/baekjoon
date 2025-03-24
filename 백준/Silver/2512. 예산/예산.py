N = int(input())
lst = list(map(int,input().split()))
M = int(input())

# s = min(lst) # 이렇게 할 경우 입력값이 모두 같으면 고장나게 됨 ex : 5 5 5 5 5, budget = 10
s = 1
e = max(lst)

ans = 0
while s <= e:
    mid = s + (e-s)//2
    budgetsum = 0
    for i in lst:
        if i <= mid:
            budgetsum += i
        else:
            budgetsum += mid
    if budgetsum <= M:
        s = mid + 1
        ans = mid
    else:
        e = mid - 1

print(ans)