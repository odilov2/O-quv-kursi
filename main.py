import classes


def main():
    print("Siz category jadvaliga ma`lumot qo`shyapsiz")
    name = input("name: ")

    data = {
        "name": name
    }

    print(classes.Category.insert_category(data))
    print("Category jadvaliga ma`lumot qo`shildi")
    print("-----------------------")


def main2():
    print("Siz kurs jadvaliga ma`lumot qo`shyapsiz")
    name = input("name: ")
    modules_count = int(input("modules_count: "))
    price = int(input("price: "))

    data = {
        "name": name,
        "modules_count": modules_count,
        "price": price
    }

    print(classes.Kurs.insert_kurs(data))
    print("Kurs jadvaliga ma`lumot qo`shildi")
    print("-----------------------")


def main3():
    print("Siz kurs_category jadvaliga ma`lumot qo`shyapsiz")
    category_id = int(input("category_id: "))
    kurs_id = int(input("kurs_id: "))

    data = {
        "category_id": category_id,
        "kurs_id": kurs_id
    }

    print(classes.Kurs_category.insert_kurs_category(data))
    print("Kurs_category jadvaliga ma`lumot qo`shildi")
    print("-----------------------")


def main4():
    print("Siz mentor jadvaliga ma`lumot qo`shyapsiz")
    first_name = input("first_name: ")
    last_name = input("last_name: ")
    birth_year = input("birth_year: ")
    salary = int(input("salary: "))
    username = input("username: ")
    password = input("password: ")

    data = {
        "first_name": first_name,
        "last_name": last_name,
        "birth_year": birth_year,
        "salary": salary,
        "username": username,
        "password": password
    }

    print(classes.Mentor.insert_mentor(data))
    print("Mentor jadvaliga ma`lumot qo`shildi")
    print("-----------------------")


def main5():
    print("Siz kurs_mentor jadvaliga ma`lumot qo`shyapsiz")
    mentor_id = int(input("mentor_id: "))
    kurs_id = int(input("kurs_id: "))

    data = {
        "mentor_id": mentor_id,
        "kurs_id": kurs_id
    }

    print(classes.Kurs_mentor.insert_kurs_mentor(data))
    print("Kurs_mentor jadvaliga ma`lumot qo`shildi")
    print("-----------------------")


def main6():
    print("Siz student jadvaliga ma`lumot qo`shyapsiz")
    first_name = input("first_name: ")
    last_name = input("last_name: ")
    birth_year = input("birth_year: ")
    username = input("username: ")
    password = input("password: ")

    data = {
        "first_name": first_name,
        "last_name": last_name,
        "birth_year": birth_year,
        "username": username,
        "password": password
    }

    print(classes.Student.insert_student(data))
    print("Student jadvaliga ma`lumot qo`shildi")
    print("-----------------------")


def main7():
    print("Siz kurs_student jadvaliga ma`lumot qo`shyapsiz")
    student_id = int(input("mentor_id: "))
    kurs_id = int(input("kurs_id: "))

    data = {
        "student_id": student_id,
        "kurs_id": kurs_id
    }

    print(classes.Kurs_student.insert_kurs_student(data))
    print("Kurs_student jadvaliga ma`lumot qo`shildi")
    print("-----------------------")


def main8():
    print("Siz lesson jadvaliga ma`lumot qo`shyapsiz")
    name = input("name: ")

    data = {
        "name": name
    }

    print(classes.Lesson.insert_lesson(data))
    print("Lesson jadvaliga ma`lumot qo`shildi")
    print("-----------------------")


def main9():
    print("Siz kurs_lesson jadvaliga ma`lumot qo`shyapsiz")
    lesson_id = int(input("lesson_id: "))
    kurs_id = int(input("kurs_id: "))

    data = {
        "lesson_id": lesson_id,
        "kurs_id": kurs_id
    }

    print(classes.Kurs_lesson.insert_kurs_lesson(data))
    print("Kurs_lesson jadvaliga ma`lumot qo`shildi")
    print("-----------------------")

    print("Ma`lumotlar muvaffaqiyatli qo`shildi")


if __name__ == "__main__":
    main()
    main2()
    main3()
    main4()
    main5()
    main6()
    main7()
    main8()
    main9()