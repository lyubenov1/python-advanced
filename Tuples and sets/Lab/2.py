def avg(values):
    return sum(values) / len(values)


n = int(input())
student_strings = [input() for _ in range(n)]

students_grades = {}

for students_string in student_strings:
    student, grade_string = students_string.split(' ')
    grade = float(grade_string)
    if student not in students_grades:
        students_grades[student] = []

    students_grades[student].append(grade)

for student, grades in students_grades.items():
    grades_avg = avg(grades)
    grades_formatted = ' '.join(f'{grade:.2f}' for grade in grades)
    grades_avg_formatted = f'{grades_avg:.2f}'
    print(f'{student} -> {grades_formatted} (avg: {grades_avg_formatted})')

