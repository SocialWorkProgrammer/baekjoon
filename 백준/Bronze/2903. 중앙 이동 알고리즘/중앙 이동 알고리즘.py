N = int(input())
def algo(n, num):
    if n > N:
        print(num**2)
    else:
        algo(n+1, num + num-1)

algo(1, 2)