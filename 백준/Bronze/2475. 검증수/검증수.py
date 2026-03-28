ans = 0
for i in list(map(int, input().split())):
    ans += i ** 2
print(ans % 10)