import logging
import datetime

from faker import Faker
import random
import psycopg2
from psycopg2 import DatabaseError

fake = Faker('uk-Ua')

NUMBER_OF_STUDENTS = 30
NUMBER_OF_GROUPS = 3
NUMBER_OF_SUBJECTS = 6
NUMBER_OF_TEACHERS = 3
GRADES_PER_SUBJECT = 3

# Підключення до бази даних
conn = psycopg2.connect(host="localhost", database="test", user="postgres", password="567234")
cur = conn.cursor()

# Додавання груп
for _ in range(NUMBER_OF_GROUPS):
    cur.execute("INSERT INTO groups (name) VALUES (%s)", (fake.word(),))

# Додавання викладачів
teacher_ids = []
for _ in range(NUMBER_OF_TEACHERS):
    cur.execute("INSERT INTO teachers (fullname) VALUES (%s) RETURNING id", (fake.name(),))
    teacher_ids.append(cur.fetchone()[0])

# Додавання предметів (кожен викладач має 2 предмети)
subject_ids = []
for teacher_id in teacher_ids:
    for _ in range(2):
        cur.execute("INSERT INTO subjects (name, teacher_id) VALUES (%s, %s) RETURNING id", (fake.word(), teacher_id))
        subject_ids.append(cur.fetchone()[0])

# Додавання студентів і оцінок
for group_id in range(1, NUMBER_OF_GROUPS + 1):
    for _ in range(NUMBER_OF_STUDENTS):
        cur.execute("INSERT INTO students (fullname, group_id) VALUES (%s, %s) RETURNING id", (fake.name(), group_id))
        student_id = cur.fetchone()[0]
        for subject_id in subject_ids:
            for _ in range(GRADES_PER_SUBJECT):
                cur.execute("INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (%s, %s, %s, %s)",
                            (student_id, subject_id, random.randint(0, 100), fake.date_between(start_date=datetime.date(2025, 1, 1), end_date=datetime.datetime.today())))

try:
    # Збереження змін
    conn.commit()
except DatabaseError as e:
    logging.error(e)
    conn.rollback()
finally:
    # Закриття підключення
    cur.close()
    conn.close()

