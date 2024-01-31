from datetime import datetime
from BASE import Database


class Category:
    def __init__(self, category_id, name):
        self.category_id = category_id
        self.name = name
        self.last_update = f"{datetime.now().date()}"

    @staticmethod
    def insert_category(data):
        query = f"""
        INSERT INTO category(name) VALUES('{data['name']}')
        """
        return Database.connect(query)


class Kurs:
    def __init__(self, kurs_id, name, modules_count, price):
        self.kurs_id = kurs_id
        self.name = name
        self.modules_count = modules_count
        self.price = price
        self.last_update = f"{datetime.now().date()}"

    @staticmethod
    def insert_kurs(data):
        query = f"""
        INSERT INTO kurs(name, modules_count, price) VALUES('{data['name']}', '{data['modules_count']}', '{data['price']}')
        """
        return Database.connect(query)


class Kurs_category:
    def __init__(self, category_id, kurs_id):
        self.kurs_id = kurs_id
        self.category_id = category_id
        self.last_update = f"{datetime.now().date()}"

    @staticmethod
    def insert_kurs_category(data):
        query = f"""
        INSERT INTO kurs_category(category_id, kurs_id) VALUES('{data['category_id']}','{data['kurs_id']}')
        """
        return Database.connect(query)


class Mentor:
    def __init__(self, mentor_id, first_name, last_name, birth_year, salary, username, password):
        self.mentor_id = mentor_id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.salary = salary
        self.username = username
        self.password = password
        self.last_update = f"{datetime.now().date()}"

    @staticmethod
    def insert_mentor(data):
        query = f"""
        INSERT INTO mentor(first_name, last_name, birth_year, salary, username, password) VALUES('{data['first_name']}', '{data['last_name']}', '{data['birth_year']}', '{data['salary']}', '{data['username']}', '{data['password']}')
        """
        return Database.connect(query)


class Kurs_mentor:
    def __init__(self, mentor_id, kurs_id):
        self.kurs_id = kurs_id
        self.mentor_id = mentor_id
        self.last_update = f"{datetime.now().date()}"

    @staticmethod
    def insert_kurs_mentor(data):
        query = f"""
        INSERT INTO kurs_mentor(mentor_id, kurs_id) VALUES('{data['mentor_id']}', '{data['kurs_id']}')
        """
        return Database.connect(query)


class Student:
    def __init__(self, student_id, first_name, last_name, birth_year, username, password):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.username = username
        self.password = password
        self.last_update = f"{datetime.now().date()}"

    @staticmethod
    def insert_student(data):
        query = f"""
        INSERT INTO student(first_name, last_name, birth_year, username, password) VALUES('{data['first_name']}', '{data['last_name']}', '{data['birth_year']}', '{data['username']}', '{data['password']}')
        """
        return Database.connect(query)


class Kurs_student:
    def __init__(self, student_id, kurs_id):
        self.kurs_id = kurs_id
        self.student = student_id
        self.last_update = f"{datetime.now().date()}"

    @staticmethod
    def insert_kurs_student(data):
        query = f"""
        INSERT INTO kurs_student(student_id, kurs_id) VALUES('{data['student_id']}', '{data['kurs_id']}')
        """
        return Database.connect(query)


class Lesson:
    def __init__(self, lesson_id, name):
        self.lesson_id = lesson_id
        self.name = name
        self.last_update = f"{datetime.now().date()}"

    @staticmethod
    def insert_lesson(data):
        query = f"""
        INSERT INTO lesson(name) VALUES('{data['name']}')
        """
        return Database.connect(query)


class Kurs_lesson:
    def __init__(self, lesson_id, kurs_id):
        self.kurs_id = kurs_id
        self.lesson_id = lesson_id
        self.last_update = f"{datetime.now().date()}"

    @staticmethod
    def insert_kurs_lesson(data):
        query = f"""
        INSERT INTO kurs_lesson(lesson_id, kurs_id) VALUES('{data['lesson_id']}', '{data['kurs_id']}')
        """
        return Database.connect(query)
