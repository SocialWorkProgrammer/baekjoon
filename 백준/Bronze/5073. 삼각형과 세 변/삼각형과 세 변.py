def tri(a, b, c):
    if max(a, b, c) >= sum([a + b + c]) - max(a, b, c):
        return 'Invalid'
    elif a == b == c:
        return 'Equilateral'
    elif a == b != c or a != b == c or a == c != b:
        return 'Isosceles'
    else:
        return 'Scalene'



a, b, c = map(int, input().split())
while a != 0:
    print(tri(a, b, c))
    a, b, c = map(int, input().split())
