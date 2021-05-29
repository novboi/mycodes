import csv

student_fields = ['roll', 'name', 'age', 'email', 'phone']
student_database = 'students_info.csv'


def display_menu():
    print("*************************************")
    print(" Welcome to Student Management System")
    print("***************************************")
    print("1. Add New Student")
    print("2. View Students Information")
    print("3. Quit")


def Add_student():
    print("////////////////////////")
    print("Add Student Information")
    print("////////////////////////")
    global student_fields
    global student_database

    student_data = []
    for field in student_fields:
        value = input("Enter " + field + ": ")
        student_data.append(value)

    with open(student_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])

    print("Data saved successfully")
    input("Press any key to continue")
    return


def view_students():
    global student_fields
    global student_database

    print("--- Student Records ---")

    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

