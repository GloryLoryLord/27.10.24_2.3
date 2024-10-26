# список с оценками
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

# множество студентов
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# преобразуем множество в отсортированный список
sorted_students = sorted(students)

# новый объявленный словарь в котором производим операцию с каждой ячейкой списка сумму grades оценок на кол-во оценок
average_grades = dict(zip(sorted_students, [
sum(grades[0]) / len(grades[0]),
sum(grades[1]) / len(grades[1]),
sum(grades[2]) / len(grades[2]),
sum(grades[3]) / len(grades[3]),
sum(grades[4]) / len(grades[4])]))


print(average_grades)


