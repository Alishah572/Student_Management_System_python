from utils import Utils as u

def show_students():

    print("    ****** Students Data ******")
    path = r'C:\Users\mueed\OneDrive\All About Python\Python\Student_Management_System_python\studentdb.mdf'

    with open(path, 'r') as f:  #  these two line is an example for fetch
        students = f.read()     #  data from db and returns a students list
        for student in students:
            print(f"   {student[1]}  |   {student[2]}   |   {student[3]}   |   {student[4]}   |   {student[5]}   |")

    input("Press any key to go back to last menu.")
    student_management_menu()


def show_courses():
    print("    ****** Courses Data ******")

    path = r'C:\Users\mueed\OneDrive\All About Python\Python\Student_Management_System_python\studentdb.mdf'
    
    with open(path, 'r') as f:  #  these two line is an example for fetch
        courses = f.read()     #  data from db and returns a students list
        for course in courses:
            print(f"   {course[0]}  |   {course[1]}   |   {course[2]}   |")
    
    input("Press any key to go back to last menu.")
    student_management_menu()


def student_management_menu():
        u.clear_screen()
        print("""
    ****** Management Menu ******
    
    1. Show Students
    2. Show Courses 
              
    Press "e" to exit.
""")
        choice = input("Enter your choice")

        match(choice):
            case '1':
                show_students()

            case '2':
                show_courses()

            case 'e':
                print("Exiting....")
                u.sleep(2)

            case _:
                print(" Invalid choice! \n Try again in 3 seconds.")
                u.sleep(3)
                student_management_menu()