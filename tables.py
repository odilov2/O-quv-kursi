from BASE import Database


def create_tables():
    category = f"""
    CREATE TABLE category(
        category_id SERIAL PRIMARY KEY,
        name VARCHAR(20),
        last_update TIMESTAMP DEFAULT NOW())
    """

    kurs = f"""
    CREATE TABLE kurs(
        kurs_id SERIAL PRIMARY KEY,
        name VARCHAR(20),
        modules_count INT,
        price NUMERIC(10, 2),
        last_update TIMESTAMP DEFAULT NOW())
    """

    kurs_category = f"""
    CREATE TABLE kurs_category(
        category_id INT REFERENCES category(category_id),
        kurs_id INT REFERENCES kurs(kurs_id),
        last_update TIMESTAMP DEFAULT NOW())
    """

    mentor = f"""
    CREATE TABLE mentor(
        mentor_id SERIAL PRIMARY KEY,
        first_name VARCHAR(30),
        last_name VARCHAR(30),
        birth_year DATE,
        salary NUMERIC(10, 2),
        username VARCHAR(20),
        password VARCHAR(20),
        last_update TIMESTAMP DEFAULT NOW())
    """

    kurs_mentor = f"""
    CREATE TABLE kurs_mentor(
        mentor_id INT REFERENCES mentor(mentor_id),
        kurs_id INT REFERENCES kurs(kurs_id),
        last_update TIMESTAMP DEFAULT NOW())
    """

    student = f"""
    CREATE TABLE student(
        student_id SERIAL PRIMARY KEY,
        first_name VARCHAR(30),
        last_name VARCHAR(30),
        birth_year DATE,
        username VARCHAR(20),
        password VARCHAR(20),
        last_update TIMESTAMP DEFAULT NOW())
    """

    kurs_student = f"""
    CREATE TABLE kurs_student(
        student_id INT REFERENCES student(student_id),
        kurs_id INT REFERENCES kurs(kurs_id),
        last_update TIMESTAMP DEFAULT NOW())
    """

    lesson = f"""
    CREATE TABLE lesson(
        lesson_id SERIAL PRIMARY KEY,
        name VARCHAR(30),
        last_update TIMESTAMP DEFAULT NOW())
    """

    kurs_lesson = f"""
    CREATE TABLE kurs_lesson(
        lesson_id INT REFERENCES lesson(lesson_id),
        kurs_id INT REFERENCES kurs(kurs_id),
        last_update TIMESTAMP DEFAULT NOW())
    """

    tables = [category, kurs, kurs_category, mentor, kurs_mentor, student, kurs_student, lesson, kurs_lesson]

    for table in tables:
        data = Database.connect(table)
        print(data)


if __name__ == "__main__":
    create_tables()


