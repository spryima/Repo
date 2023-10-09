from sqlalchemy import create_engine, ForeignKey, Column, String, SmallInteger, Integer, Date
from sqlalchemy.orm import declarative_base



Base = declarative_base()

class Group(Base):
    __tablename__ = 'groups'
    id = Column(SmallInteger, primary_key=True)
    group_name = Column(String(255), unique=True, nullable=False)
    
class Student(Base):
    __tablename__ = 'students'
    id = Column(SmallInteger, primary_key=True)
    student_name = Column(String(255), nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id', onupdate="CASCADE"))

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(SmallInteger, primary_key=True)
    subj_name = Column(String(255), unique=True, nullable=False)
    
class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(SmallInteger, primary_key=True)
    teacher_name = Column(String(255), nullable=False)
    subj_name_id = Column(Integer, ForeignKey('subjects.id', onupdate="CASCADE"))
    
class Scoreboard(Base):
    __tablename__ = 'scoreboard'
    id = Column(SmallInteger, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    subj_name = Column(String(255), ForeignKey('subjects.subj_name'), nullable=False)
    grade = Column(Integer, nullable=False)
    date_received = Column(Date, nullable=False)


