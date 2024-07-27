import mysql.connector as mysql

db = mysql.connect(
    #secrets
)

cursor = db.cursor(dictionary=True)

# 1 INSERT INTO students (name, second_name) VALUES ('Arnold', 'Arni_Tester')
query_1 = 'INSERT INTO students (name, second_name) VALUES (%s, %s)'
values_1 = ('Arnold', 'Arni_Tester')
cursor.execute(query_1, values_1)
student_id = cursor.lastrowid

# 2
# INSERT INTO books (title) VALUES ('The first book for Arni')
# INSERT INTO books (title) VALUES ('The secons book for Arni')
# UPDATE books SET taken_by_student_id = 1400
# WHERE title = 'The first book for Arni' or title = 'The secons book for Arni'
query_2 = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
values_2 = [('The first book for Arni', student_id), ('The second book for Arni', student_id)]
cursor.executemany(query_2, values_2)

# 3
# INSERT INTO `groups` (title, start_date, end_date) VALUES ('Group for Arni', 'May 2024', 'Sep 2024')
# UPDATE students SET group_id = 1398 WHERE id = 1400
query_3_1 = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
values_3_1 = ('Group for Arni', 'May 2024', 'Sep 2024')
cursor.execute(query_3_1, values_3_1)
new_group_id = cursor.lastrowid

query_3_2 = "UPDATE students SET group_id = %s WHERE id = %s"
values_3_2 = (new_group_id, student_id)
cursor.execute(query_3_2, values_3_2)

# 4
# INSERT INTO subjets (title) VALUES ('Math_for_Arni')
# INSERT INTO subjets (title) VALUES ('Geo_for_Arni')
query_4 = 'INSERT INTO subjets (title) VALUES (%s)'
values_4_1 = ['Math_for_Arni']
values_4_2 = ['Geo_for_Arni']

cursor.execute(query_4, values_4_1)
sub_1_id = cursor.stored_results()

cursor.execute(query_4, values_4_2)
sub_2_id = cursor.stored_results()

# 5
# INSERT INTO lessons (title, subject_id) VALUES ('Lesson_1 for Math_for_Arni', 1863)
# INSERT INTO lessons (title, subject_id) VALUES ('Lesson_2 for Math_for_Arni', 1863)
# INSERT INTO lessons (title, subject_id) VALUES ('Lesson_1 for Geo_for_Arni', 1864)
# INSERT INTO lessons (title, subject_id) VALUES ('Lesson_2 for Geo_for_Arni', 1864)
query_5 = "INSERT lessons (title, subject_id) VALUES (%s, %s)"

values_5_1 = ['Lesson_1 for Math_for_Arni', sub_1_id]
values_5_2 = ['Lesson_2 for Math_for_Arni', sub_1_id]
values_5_3 = ['Lesson_1 for Geo_for_Arni', sub_2_id]
values_5_4 = ['Lesson_2 for Geo_for_Arni', sub_2_id]

cursor.execute(query_5, values_5_1)
less_1_id = cursor.stored_results()

cursor.execute(query_5, values_5_2)
less_2_id = cursor.stored_results()

cursor.execute(query_5, values_5_3)
less_3_id = cursor.stored_results()

cursor.execute(query_5, values_5_4)
less_4_id = cursor.stored_results()

# 6
# INSERT INTO marks (value, lesson_id, student_id) VALUES (5, 4234, 1400)
# INSERT INTO marks (value, lesson_id, student_id) VALUES (9, 4235, 1400)
# INSERT INTO marks (value, lesson_id, student_id) VALUES (1, 4236, 1400)
# INSERT INTO marks (value, lesson_id, student_id) VALUES (7, 4237, 1400)

query_6 = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
values_6_1 = [5, less_1_id, student_id]
values_6_2 = [7, less_2_id, student_id]
values_6_3 = [9, less_3_id, student_id]
values_6_4 = [2, less_4_id, student_id]

cursor.execute(query_6, values_6_1)
mark_1_id = cursor.stored_results()

cursor.execute(query_6, values_6_1)
mark_2_id = cursor.stored_results()

cursor.execute(query_6, values_6_2)
mark_3_id = cursor.stored_results()

cursor.execute(query_6, values_6_3)
mark_4_id = cursor.stored_results()

# 7 SELECT m.value FROM marks m WHERE student_id = 1400
query_7 = f"SELECT m.value FROM marks m WHERE student_id = {student_id}"
cursor.execute(query_7)
print(cursor.fetchall())

# 8 SELECT b.title FROM books b WHERE b.taken_by_student_id = 1400
query_8 = f"SELECT b.title FROM books b WHERE b.taken_by_student_id = {student_id}"
cursor.execute(query_8)
print(cursor.fetchall())

# 9
query_9 = f'''
SELECT s.id Student_id, s.name First_name, s.second_name Second_name, g.title Grpoup_title, g.start_date Start_date, 
g.end_date End_date, b.title Book_title, mls.Mark Mark_value, mls.Lesson_id Lesson_id, mls.Subject_title Subject_title
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
WHERE s.id = {student_id}
'''
cursor.execute(query_9)
print(cursor.fetchall())

db.commit()
db.close()
