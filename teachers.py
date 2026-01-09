from utils import Utils as u
import database as db

def teacher_management_menu():
    u.clear_screen()
    print("""
    ****** Teacher Management Menu ******
    
    1. Show All Teachers
    2. New Admission (Student Enrollment)
              
    Press "e" to exit.
""")
    choice = input("    Enter your choice: ")

    match(choice):
        case '1':
            show_teachers()

        case '2':
            new_addmission()

        case 'e':
            print("    Returning to main menu...")
            u.sleep(1)

        case _:
            print("    Invalid choice! \n    Try again in 3 seconds.")
            u.sleep(3)
            teacher_management_menu()

def show_teachers():
    u.clear_screen()
    # Fetch all teachers from the database
    # Note: You may need to add get_all_teachers to database.py if not already there
    con = db.create_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM teachers")
    teachers = cur.fetchall()
    cur.close()
    con.close()

    print("    " + "="*125)
    print("    {:^125}".format("TEACHER'S DIRECTORY"))
    print("    " + "="*125)

    if not teachers:
        print("\n    [!] No teacher records found.")
    else:
        # Define Headers
        headers = ["ID", "Full Name", "Father Name", "Gender", "Phone", "Course Specialty"]
        print(f"    {headers[0]:<5} | {headers[1]:<25} | {headers[2]:<20} | {headers[3]:<10} | {headers[4]:<15} | {headers[5]:<25}")
        print("    " + "-"*125)

        for t in teachers:
            # Index mapping: 0:id, 1:first, 2:last, 3:father, 4:gender, 5:phone, 8:course
            full_name = f"{t[1]} {t[2]}"
            print(f"    {str(t[0]):<5} | {full_name:<25} | {t[3]:<20} | {t[4]:<10} | {t[5]:<15} | {t[8]:<25}")

    print("    " + "="*125)
    input("\n    Press any key to go back to last menu.")
    teacher_management_menu()

def approval(admission_data):
    # This sends the data to the students table in the database
    print("\n    Sending for approval...")
    u.sleep(1)
    db.db_add_student(admission_data)
    print("    ✅ Admission record saved successfully!")
    u.sleep(2)

def new_addmission():
    u.clear_screen()
    print("    " + "="*50)
    print("    {:^50}".format("STUDENT ADMISSION FORM"))
    print("    " + "="*50)

    first_name = input("    First Name       : ")
    last_name  = input("    Last Name        : ") 
    father_name= input("    Father Name      : ") 
    gender     = input("    Gender           : ") 
    phone_no   = input("    Phone No.        : ") 
    address    = input("    Address          : ")    
    email      = input("    Email Address    : ") 
    course     = input("    Course to Enroll : ") 

    admission_form = [first_name, last_name, father_name, gender, phone_no, address, email, course]
    
    print("\n    1. Confirm and Save")
    print("    2. Discard and Go Back")
    
    choice = input("\n    Enter your choice: ")

    if choice == '1':
        approval(admission_form)
        teacher_management_menu()
    else:
        print("    Admission discarded.")
        u.sleep(1)
        teacher_management_menu()