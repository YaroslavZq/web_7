import random

from faker import Faker

from database.db import session
from database.models import Group, Student, Teacher, Subject, Mark

fake = Faker()
Q_GROUP = 3 # кількість груп
Q_STUDENT = 50 # кількість студентів
Q_TEACHER = 5 # кількість викладачів
Q_SUBJECT = 8 # кількість предметів
Q_MARK = 20 # кількість оцінок в 1 студента


def create_group(quantity):
	for i in range(quantity):
		group = Group(
			name=f"Group: {i}"
		)
		session.add(group)
	session.commit()


def create_teacher(quantity):
	for _ in range(quantity):
		teacher = Teacher(
			teacher=fake.name(),
		)
		session.add(teacher)
	session.commit()


def create_student(quantity):
	groups = session.query(Group).all()
	for _ in range(quantity):
		student = Student(
			student=fake.name(),
			group_id=random.choice(groups).id
		)
		session.add(student)
	session.commit()


def create_subject(quantity):
	teachers = session.query(Teacher).all()
	for _ in range(quantity):
		subject = Subject(
			subject=f"Subject for {fake.job()}",
			teacher_id=random.choice(teachers).id
		)
		session.add(subject)
	session.commit()


def create_mark(quantity):
	students = session.query(Student).all()
	subjects = session.query(Subject).all()
	for student in students:
		for _ in range(quantity):
			mark = Mark(
				mark=fake.random_int(min=1, max=12),
				date=fake.date_between(start_date='-1y'),
				student_id=student.id,
				subject_id=random.choice(subjects).id
			)
			session.add(mark)
	session.commit()


if __name__ == "__main__":
	create_teacher(Q_TEACHER)
	create_group(Q_GROUP)
	create_subject(Q_SUBJECT)
	create_student(Q_STUDENT)
	create_mark(Q_MARK)

