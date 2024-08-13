import mysql.connector as mysql
import os
import dotenv
import csv


dotenv.load_dotenv(override=True)

db = mysql.connect(
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor()
cursor.execute('SELECT * FROM students')
data = cursor.fetchall()

query_9 = f'''
SELECT s.name First_name, s.second_name Second_name, g.title Grpoup_title, b.title Book_title, 
mls.Subject_title Subject_title, mls.Lesson_id Lesson_id,
mls.Mark Mark_value
FROM students s
JOIN `groups` g ON s.group_id = g.id
JOIN books b ON s.id = b.taken_by_student_id
JOIN (
    SELECT j1.Stud_id, j1.markid Mark_id, j1.Mark, j1.t1 Lesson_id, j2.stil Subject_title FROM (
        SELECT m.id markid, m.value Mark, m.student_id Stud_id, l.id lid, l.title t1 FROM marks m
            JOIN lessons l ON m.lesson_id = l.id) j1
            JOIN (
                SELECT l.id lid2, l.title t2, s.title stil FROM lessons l
                    JOIN subjets s ON l.subject_id = s.id
                ) j2 ON j1.lid = j2.lid2
        ) mls ON s.id = mls.Stud_id
'''
cursor.execute(query_9)
data_db = cursor.fetchall()

file_path = r"C:\Users\serge\PycharmProjects\SSovras\homework\eugene_okulik\Lesson_16\hw_data\data.csv"
with open(file_path,  newline='') as csv_file:
    file_data = csv.reader(csv_file)
    for row in file_data:
        if tuple(row) not in data_db:
            print(row)

db.close()
