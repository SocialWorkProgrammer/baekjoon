import sys
input = sys.stdin.readline

# 전략 : 중간에 수가 반복되는 점을 이용하여 반복될 때 멈춘 후 계산
A, B, C = map(int, input().split())
lst = []  # 수를 넣을 빈 리스트
X = 1

def div(A, B, C):
    if B == 1:
        return A % C
    if B % 2 == 1:
        return (div(A, B//2, C) ** 2) * A % C
    else:
        return div(A, B//2, C) ** 2 % C
print(div(A,B,C))


# 시간초과
# 수들이 반복될 때까지 리스트에 계속 추가
# while (A**X) % C not in lst:
#     lst.append(A**X % C)
#     X += 1
#     if (A**X) % C in lst:
#         ans = B % len(lst) - 1
#         print(lst[ans])
#         break


