from datetime import date
from random import randint, choice

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Group, Student, Subject, Teacher, Scoreboard

NUMBER_OF_GROUPS = 3
NUMBER_OF_STUDENTS = 50
NUMBER_OF_SUBJECTS = 8
NUMBER_OF_TEACHERS = 5
NUMBER_OF_MARKS = 20


def generate_fake_data() -> tuple:
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


def prepare_data(groups, students, subjects, teachers, marks, fake_dates) -> tuple:
    
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


def insert_data_to_db(groups, students, subjects, teachers, marks) -> None:

    engine = create_engine('postgresql://postgres:121212@localhost:5433/postgres_alch')
    Base.metadata.create_all(engine)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    try:
        
        group_objects = [Group(group_name=group[0]) for group in groups]
        session.add_all(group_objects)
        session.commit()  

        student_objects = [Student(student_name=student[0], group_id=student[1]) for student in students]
        session.add_all(student_objects)
        session.commit()

        subject_objects = [Subject(subj_name=subject[0]) for subject in subjects]
        session.add_all(subject_objects)
        session.commit()

        teacher_objects = [Teacher(teacher_name=teacher[0], subj_name_id=teacher[1]) for teacher in teachers]
        session.add_all(teacher_objects)
        session.commit()

        mark_objects = [Scoreboard(student_id=mark[0], subj_name=mark[1], grade=mark[2], date_received=mark[3]) for mark in marks]
        session.add_all(mark_objects)
        session.commit()

        print("Data inserted successfully")

    except Exception as e:
        session.rollback()  
        print(f"An error occurred: {e}")

    finally:
        session.close()  


if __name__ == "__main__":

    groups, students, subjects, teachers, marks = prepare_data(*generate_fake_data())
    insert_data_to_db(groups, students, subjects, teachers, marks)