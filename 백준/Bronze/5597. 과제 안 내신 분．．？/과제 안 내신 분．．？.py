students = [i for i in range(1, 31)]
hw = [int(input()) for _ in range(28)]
for i in hw:
    if i in students:
        students.remove(i)
students.sort()
print(students[0])
print(students[1])