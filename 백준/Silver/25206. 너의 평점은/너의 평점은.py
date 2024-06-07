keys = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
values = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

gradesys = dict(zip(keys, values))

gradelst = [] # 학점 * 과목평점
grade = []
for i in range(20):
    majorscore = list(map(str, input().split(' ')))
    if majorscore[2] != 'P':
        gradelst.append(int(majorscore[1][0]) * gradesys[majorscore[2]])
        grade.append(int(majorscore[1][0]))
print(sum(gradelst)/sum(grade))