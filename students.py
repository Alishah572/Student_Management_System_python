from utils import Utils as u
import database as db

def show_students():
    u.clear_screen()
    print("    " + "="*115)
    print("    {:^115}".format("STUDENTS LIST"))
    print("    " + "="*115)

    # Fetch data from database
    students = db.get_all_students()

    if not students:
        print("\n    [!] No student records found in the database.")
    else:
        # Define aligned headers
        # Indices based on your schema: 0:id, 1:first, 2:last, 3:father, 4:gender, 5:phone, 8:course
        headers = ["ID", "Name", "Father Name", "Gender", "Phone", "Course Enrolled"]
        print(f"    {headers[0]:<5} | {headers[1]:<20} | {headers[2]:<20} | {headers[3]:<10} | {headers[4]:<15} | {headers[5]:<20}")
        print("    " + "-"*115)

        for student in students:
            full_name = f"{student[1]} {student[2]}"
            print(f"    {str(student[0]):<5} | {full_name:<20} | {student[3]:<20} | {student[4]:<10} | {student[5]:<15} | {student[8]:<20}")

    print("    " + "="*115)
    input("\n    Press any key to go back to last menu.")
    student_management_menu()


def show_courses():
    u.clear_screen()
    print("    " + "="*80)
    print("    {:^80}".format("AVAILABLE COURSES"))
    print("    " + "="*80)

    # Fetch data from database
    courses = db.db_get_all_courses()

    if not courses:
        print("\n    [!] No courses found.")
    else:
        # Headers: ID, Course Name, Department
        print(f"    {'ID':<10} | {'Course Name':<40} | {'Department':<20}")
        print("    " + "-"*80)

        for course in courses:
            print(f"    {str(course[0]):<10} | {course[1]:<40} | {course[2]:<20}")

    print("    " + "="*80)
    input("\n    Press any key to go back to last menu.")
    student_management_menu()


def student_management_menu():
    u.clear_screen()
    print("""
    ****** Student Management Menu ******
    
    1. Show My Info / All Students
    2. Show Available Courses 
              
    Press "e" to exit.
""")
    choice = input("    Enter your choice: ")

    match(choice):
        case '1':
            show_students()

        case '2':
            show_courses()

        case 'e':
            print("    Returning to main menu...")
            u.sleep(1)
            # This will return control back to the main loop in main.py

        case _:
            print("    Invalid choice! \n    Try again in 3 seconds.")
            u.sleep(3)
            student_management_menu()