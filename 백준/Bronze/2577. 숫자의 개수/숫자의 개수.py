ans = 1
for i in range(3):
    ans *= int(input())
for num in range(10):
    print(str(ans).count(str(num)))