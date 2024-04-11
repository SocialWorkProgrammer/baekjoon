Nlst = [int(input()) for _ in range(10)]

remains = []
for i in Nlst:
    if i % 42 not in remains:
        remains.append(i % 42)
    else:
        pass
print(len(remains))