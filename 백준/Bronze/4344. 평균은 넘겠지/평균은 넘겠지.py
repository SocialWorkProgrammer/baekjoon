import sys
input = sys.stdin.readline

N = int(input())
for tc in range(N):
    sn, *students = list(map(int, input().split()))
    avg = sum(students) / sn
    ans = sum([1 for student in students if student > avg])/sn * 100
    print(f'{ans:.3f}%')