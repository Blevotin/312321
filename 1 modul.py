grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_grades = {'Johnny': grades[0], 'Bilbo': grades[1], 'Steve': grades[2], 'Khendrik': grades[3], 'Aaron': grades[4],}
students_sort = sorted(students)

y = len(students_sort)

sr = []
for x in grades:
    sr1_num = 0
    for g in x:
        sr1_num += g
    sr.append(round(sr1_num / len(x), 1))
print(sr)
sr = {k: v for k, v in zip( students_sort, sr)}
print(sr)











