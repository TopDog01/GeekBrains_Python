#Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
#Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
#Input: 5 -> 1 3 3 3 4
#Output: 1 3 3 3 1
#
# def replace_grades(grades_list):
#     # Находим максимальную и минимальную оценки
#     max_grade = max(grades_list)
#     min_grade = min(grades_list)
#
#     # Заменяем все минимальные оценки на максимальные, и наоборот
#     new_grades = [max_grade if grade == min_grade else min_grade if grade == max_grade else grade for grade in grades_list]
#
#     return new_grades
#     # Вводим оценки Василия
# grades = [1, 3, 3, 3, 4]
# result = replace_grades(grades)
# print(*result)

lst1 = [1, 3, 3, 3, 4]
min_grade = min(lst1)
max_grade = max(lst1)
lst2 = []
for grade in lst1:
    if grade == max_grade:
        lst2.append(min_grade)
    else:
        lst2.append(grade)
print(lst2)

print([min_grade if grade == max_grade else grade for grade in lst1])

def func(lst1, lst2=[], min_grade=min(lst1), max_grade=max(lst1)):
    if len(lst1) == 0:
        return lst2
    if lst1[0] == max_grade:
        lst2.append(min_grade)
    else:
        lst2.append(lst1[0])
    return func(lst1[1:], lst2)

print(func(lst1))