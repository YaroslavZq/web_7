from sqlalchemy import Column, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime


Base = declarative_base()


# Таблиця groups, зберігання кількості груп студентів
class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)

    students = relationship('Student', back_populates='groups', passive_deletes=True)


# Таблиця students, зберігання студентів з привязкою до групи
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    student = Column(String(255), nullable=False, unique=True)
    group_id = Column(Integer, ForeignKey(Group.id, ondelete="SET NULL", onupdate="CASCADE"))

    groups = relationship("Group", back_populates='students', passive_deletes=True)
    marks = relationship("Mark", back_populates="students", passive_deletes=True)


# Таблиця teachers, зберігання вчителів
class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    teacher = Column(String(255), nullable=False, unique=True)

    subjects = relationship('Subject', back_populates='teachers', passive_deletes=True)


# Таблиця subjects, зберігання предметів з привязкою до викладача
class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    subject = Column(String(255), nullable=False, unique=True)
    teacher_id = Column(Integer, ForeignKey(Teacher.id, ondelete="SET NULL", onupdate="CASCADE"))

    teachers = relationship("Teacher", back_populates='subjects', passive_deletes=True)
    marks = relationship("Mark", back_populates="subjects", passive_deletes=True)


# Таблиця marks, зберігання оцінок з привязкою до студента та предмета по якому виставлено оцінку
class Mark(Base):
    __tablename__ = "marks"
    id = Column(Integer, primary_key=True)
    mark = Column(Integer, nullable=False)
    date = Column(DateTime, default=func.now())
    subject_id = Column(Integer, ForeignKey(Subject.id, ondelete="CASCADE", onupdate="CASCADE"))
    student_id = Column(Integer, ForeignKey(Student.id, ondelete="CASCADE", onupdate="CASCADE"))

    subjects = relationship("Subject", back_populates='marks', passive_deletes=True)
    students = relationship("Student", back_populates="marks", passive_deletes=True)
