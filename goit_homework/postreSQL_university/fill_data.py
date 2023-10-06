from datetime import date
from random import randint, choice

from faker import Faker
import psycopg2

NUMBER_OF_GROUPS = 3
NUMBER_OF_STUDENTS = 50
NUMBER_OF_SUBJECTS = 8
NUMBER_OF_TEACHERS = 5
NUMBER_OF_MARKS = 20


def generate_fake_data() -> tuple():
    fake_groups = ['lr-14', 'ps-32' , 'zs-12'] 
    fake_students = []
    fake_teachers = []
    fake_subjects = [
        "Українська мова",
        "Історія України", 
        "Логіка", 
        "Вища математика", 
        "Фізика", 
        "Хімія", 
        "Теорія алгоритмів", 
        "Електротехніка та електроніка"
        ]
    fake_marks = []
    fake_dates = []
    
    fake_data = Faker('uk-UA')

    for _ in range(NUMBER_OF_STUDENTS):
        fake_students.append(fake_data.name())

    for _ in range(NUMBER_OF_TEACHERS):
        fake_teachers.append(fake_data.name())

    for _ in range(NUMBER_OF_MARKS):
        fake_marks.append(randint(1,12))
        fake_dates.append(fake_data.date_between_dates(date(2022, 1, 1), date(2022, 12, 31)))

    return fake_groups, fake_students, fake_subjects, fake_teachers, fake_marks, fake_dates


def prepare_data(groups, students, subjects, teachers, marks, fake_dates) -> tuple():
    for_groups = []
    for gr in groups:
        for_groups.append((gr,))
    
    for_students = []
    for st in students:
        for_students.append((st, randint(1, NUMBER_OF_GROUPS)))

    for_subjects = []
    for sb in subjects:
        for_subjects.append((sb,))        
    
    for_teachers = []
    for tc in teachers:
        for_teachers.append((tc, randint(1, randint(1, NUMBER_OF_SUBJECTS))))
    
    for_marks = []
    for _ in for_students:
        for mk in marks:
            for_marks.append((
                randint(1, NUMBER_OF_STUDENTS), 
                choice(subjects), 
                mk, 
                choice(fake_dates)
                ))

    return for_groups, for_students, for_subjects, for_teachers, for_marks


def read_sql_file():
    with open('SQL_queries/university.sql', 'r') as file:
        return file.read().split(';')[:-1]


def create_tables(cursor):
    queries = read_sql_file()
    
    for query in queries:
        cursor.execute(query)


def insert_data_to_db(groups, students, subjects, teachers, marks) -> None:
    try:
        conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='121212',
            host='localhost',
            port='5432'
        )
        
        cursor = conn.cursor()

        create_tables(cursor)
        
        for group in groups:
            cursor.execute("INSERT INTO groups (group_name) VALUES (%s)", group)

        for student in students:
            cursor.execute("INSERT INTO students (student_name, group_id) VALUES (%s, %s)", student)

        for subject in subjects:
            cursor.execute("INSERT INTO subjects (subj_name) VALUES (%s)", subject)

        for teacher in teachers:
            cursor.execute("INSERT INTO teachers (teacher_name, subj_name_id) VALUES (%s, %s)", teacher)

        for mark in marks:
            cursor.execute("INSERT INTO scoreboard (student_id, subj_name, grade, date_received) VALUES (%s, %s, %s, %s)", mark)


        conn.commit()
        
        print("Data inserted successfully")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()




if __name__ == "__main__":

    groups, students, subjects, teachers, marks = prepare_data(*generate_fake_data())
    insert_data_to_db(groups, students, subjects, teachers, marks)