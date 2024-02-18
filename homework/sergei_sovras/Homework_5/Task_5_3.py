students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
students_to_str = ', '.join(students)
subjects_to_str = ', '.join(subjects)
answer = f'Students {students_to_str} study these subjects: {subjects_to_str}'
print(answer)
