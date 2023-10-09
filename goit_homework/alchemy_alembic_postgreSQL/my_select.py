from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from models import Group, Student, Subject, Teacher, Scoreboard

engine = create_engine('postgresql://postgres:121212@localhost:5433/postgres_alch')
Session = sessionmaker(bind=engine)
session = Session()

def select_1():
    result = session.query(Student.student_name, func.avg(Scoreboard.grade))\
                    .join(Scoreboard, Student.id == Scoreboard.student_id)\
                    .group_by(Student.student_name)\
                    .order_by(func.avg(Scoreboard.grade).desc())\
                    .limit(5).all()
    return result

def select_2():
    result = session.query(Student.student_name, func.avg(Scoreboard.grade))\
                    .join(Scoreboard, Student.id == Scoreboard.student_id)\
                    .filter(Scoreboard.subj_name == 'Фізика')\
                    .group_by(Student.student_name)\
                    .order_by(func.avg(Scoreboard.grade).desc())\
                    .first()
    return result

def select_3():
    result = session.query(Group.group_name, func.avg(Scoreboard.grade))\
                    .join(Student, Group.id == Student.group_id)\
                    .join(Scoreboard, Student.id == Scoreboard.student_id)\
                    .filter(Scoreboard.subj_name == 'Фізика')\
                    .group_by(Group.group_name).all()
    return result

def select_4():
    result = session.query(func.avg(Scoreboard.grade)).all()
    return result

def select_5():
    result = session.query(Teacher.teacher_name, Subject.subj_name)\
                    .join(Subject, Teacher.subj_name_id == Subject.id).all()
    return result

def select_6(group_name):
    result = session.query(Student.student_name)\
                    .join(Group, Student.group_id == Group.id)\
                    .filter(Group.group_name == group_name).all()
    return result

def select_7(group_name, subj_name):
    result = session.query(Scoreboard.grade)\
                    .join(Student, Scoreboard.student_id == Student.id)\
                    .join(Group, Student.group_id == Group.id)\
                    .filter(Group.group_name == group_name, Scoreboard.subj_name == subj_name).all()
    return result

def select_8(teacher_name):
    result = session.query(func.avg(Scoreboard.grade))\
                    .join(Subject, Scoreboard.subj_name == Subject.subj_name)\
                    .join(Teacher, Subject.id == Teacher.subj_name_id)\
                    .filter(Teacher.teacher_name == teacher_name).all()
    return result

def select_9(student_name):
    result = session.query(Scoreboard.subj_name)\
                    .join(Student, Scoreboard.student_id == Student.id)\
                    .filter(Student.student_name == student_name).all()
    return result

def select_10(student_name, teacher_name):
    result = session.query(Scoreboard.subj_name).distinct()\
                    .join(Student, Scoreboard.student_id == Student.id)\
                    .join(Subject, Scoreboard.subj_name == Subject.subj_name)\
                    .join(Teacher, Subject.id == Teacher.subj_name_id)\
                    .filter(Student.student_name == student_name, Teacher.teacher_name == teacher_name).all()
    return result

if __name__ == "__main__":
    print(select_1(), end="\n\n")
    print(select_2(), end="\n\n")
    print(select_3(), end="\n\n")
    print(select_4(), end="\n\n")
    print(select_5(), end="\n\n")
    print(select_6('lr-14'), end="\n\n")
    print(select_7('lr-14', 'Фізика'), end="\n\n")
    print(select_8('Спас Туркало'), end="\n\n")
    print(select_9('Юстим Зінчук'), end="\n\n")
    print(select_10('Юстим Зінчук', 'Спас Туркало'), end="\n\n")
