def lunar(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return 1
            return 0
        return 1
    else:
        return 0

N = int(input())
print(lunar(N))