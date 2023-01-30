from sqlalchemy import func, desc, and_

from database.db import session
from database.models import Student, Mark, Subject, Teacher, Group


def select_1():
	return session.query(Student.student, func.round(func.avg(Mark.mark), 2).label('avg_grade')).select_from(Mark)\
		.join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()


def select_2():
	return session.query(Student.student, func.round(func.avg(Mark.mark), 2).label('avg_grade'), Subject.subject)\
		.select_from(Mark).join(Student, Subject).where(Subject.id == 3).group_by(Student.id, Subject.id)\
		.order_by(desc('avg_grade')).limit(1).all()


def select_3():
	return session.query(func.round(func.avg(Mark.mark), 2).label('avg_grade'), Subject.subject, Group.name)\
		.select_from(Mark).join(Student, Subject, Group).where(Subject.id == 3).group_by(Group.id, Subject.id)\
		.order_by(desc('avg_grade')).all()


def select_4():
	return session.query(func.round(func.avg(Mark.mark), 2).label('avg_grade')).select_from(Mark).all()


def select_5():
	return session.query(Subject.subject, Teacher.teacher).select_from(Subject).join(Teacher)\
		.group_by(Subject.id, Teacher.id).all()


def select_6():
	return session.query(Group.name, Student.student).select_from(Student).join(Group).order_by(Group.name).all()


# not done
def select_7():
	return session.query(Subject.subject, Group.name, Student.student, Mark.mark).select_from(Mark)\
		.join(Student, Subject, Group).where(Subject.id == 3).order_by(Student.student).all()


def select_8():
	return session.query(Teacher.teacher, func.round(func.avg(Mark.mark), 2).label('avg_grade')).select_from(Mark)\
		.join(Subject, Teacher).where(Teacher.id == 2).group_by(Teacher.id).all()


def select_9():
	return session.query(Student.student, Subject.subject).select_from(Mark)\
		.join(Student, Subject).where(Student.id == 28).group_by(Subject.id, Student.id).order_by(Subject.subject).all()


def select_10():
	return session.query(Student.student, Subject.subject, Teacher.teacher).select_from(Mark)\
		.join(Student, Subject, Teacher).where(and_(Student.id == 22, Teacher.id == 1))\
		.group_by(Subject.id, Student.id, Teacher.id).order_by(Subject.subject).all()


def select_11():
	return session.query(Student.student, Teacher.teacher, func.round(func.avg(Mark.mark), 2).label('avg_grade'))\
		.select_from(Mark).join(Student, Subject, Teacher).where(and_(Student.id == 23, Teacher.id == 1))\
		.group_by(Teacher.id, Student.id).all()


def select_12():
	return session.query(Group.name, Student.student, Mark.mark, Mark.date, Subject.subject)\
		.select_from(Mark).join(Student, Subject, Group).where(and_(Subject.id == 7, Group.id == 3,
	        Mark.date == session.query(func.max(Mark.date)).select_from(Mark).join(Subject, Student, Group)\
	        .where(and_(Subject.id == 7, Group.id == 3)).group_by(Subject.id, Group.id))).all()


if __name__ == '__main__':
	s = select_12()
	print(s)
