import os
import datetime


homework_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))  # Homework path
eugene_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')  # Eugene's path


def return_lines(file_path):
    with open(file_path, 'r') as current_file:
        for line in current_file.readlines():
            yield line


def get_datetime(line):
    raw_date_f = line.split(' - ')[0].split('. ')[1]
    date_f = datetime.datetime.strptime(raw_date_f, '%Y-%m-%d %H:%M:%S.%f')
    return date_f


for lines in return_lines(eugene_file_path):
    line_id = lines.split('. ')[0]

    if line_id == '1':
        print("Answer_1 ", get_datetime(lines) + datetime.timedelta(weeks=1))

    if line_id == '2':
        day_of_week = get_datetime(lines).weekday()
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        print("Answer_2:", days[day_of_week - 1])

    if line_id == '3':
        print("Answer_3:", datetime.datetime.now() - get_datetime(lines))
