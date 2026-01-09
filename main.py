from utils import Utils as u
from crypto_utils import generate_key, encrypt_message, decrypt_message, get_chars
from teachers import teacher_management_menu
from students import student_management_menu

import database as db

# Global variable to track which panel (Principal, Teacher, Student) is active
current_role_panel = 0 

def save_data(username, email, password):
    # 1. Generate Encryption Key
    chars, key_list = generate_key()
    
    # 2. Encrypt the password
    cipher_text = encrypt_message(password, chars, key_list)
    
    # 3. Convert key list to string for storage
    key_str = "".join(key_list)
    
    # 4. Save to Database
    success = db.db_save_user(username, email, cipher_text, key_str, current_role_panel)
    
    if success:
        print("    Signup Successful!")
    else:
        print("    Signup Failed (Username might exist).")
    u.sleep(2)

def user_Check(username, password) -> bool:
    # 1. Fetch credentials from DB
    data = db.db_get_user_credentials(username)
    
    if not data:
        print("    User not found.")
        u.sleep(2)
        return False
        
    stored_hash, key_str, role_id = data
    
    # 2. Reconstruct key
    key_list = list(key_str)
    chars = get_chars()
    
    # 3. Decrypt stored password
    decrypted_pass = decrypt_message(stored_hash, chars, key_list)
    
    # 4. Verify password and Role
    if decrypted_pass == password:
        if role_id == current_role_panel:
            return True
        else:
            print(f"    Access Denied. Authorization failed for this role.")
            u.sleep(2)
            return False
    else:
        print("    Incorrect Password.")
        u.sleep(2)
        return False

def email_check(email, username) -> bool:
    # Check if email exists in DB
    exists = db.db_email_exists(email)
    if exists:
        print("    Email already registered.")
        return False
    return True

def Login_Signup(num):
    global current_role_panel
    current_role_panel = num
    u.clear_screen()
    role_name = "Principal" if num == 1 else "Teacher" if num == 2 else "Student"
    
    print(f"""
    **** Welcome to {role_name} Login & Signup ****
        
        1. Login
        2. Signup
    
    Enter any key to go back to main menu.
""")
    choice = str(input("Enter your choice. "))

    match (choice.strip()):
        case '1':
            login(num)
        case '2':
            signup(num)
        case _:
            main()

def login(num):
    u.clear_screen()
    print("""
    *********** Login ***********
    
    Enter your details:
          
""")
    username = input("    Username: ")
    password = input("    Password: ")
    
    value : bool = user_Check(username, password)

    if value and num == 2:
        teacher_management_menu()

    if value and num == 3:
        student_management_menu()

    if value and num == 1:
        obj_principal = Principal()
        obj_principal.main()

def signup(panel):
    while(True):
        u.clear_screen()
        print("""
        *********** Signup ***********
        
        Enter your details:
            
    """)
        username = input("    Username: ")
        email = input("    Email: ")
        password = input("    Password: ")

        emailCheck = email_check(email, username)
        
        if emailCheck:
            save_data(username,email,password)
            login(panel)
            break
        else:
            print("Invalid Email or User exists.")
            u.sleep(3)
            return
  

# ------------------------------------------------------ #

    
class Record_teacher():

    def save_teacher(self, enrollment):
        db.db_add_teacher(enrollment)
        print("Enrollment saved successfully.")
        u.sleep(1)

    def new_teacher(self):
            u.clear_screen()
            print("    ****** Introducing New Teacher ******")
            print("\n")
            first_name = input("    First name : ")
            last_name = input("    Last name : ")
            father_name = input("    Father name : ")
            gender = input("    Gender : ")
            phone_no = input("    Phone no. : ")
            address = input("    Address : ")
            email = input("    Email Address : ")
            course_teach = input("    Course you can teach : ")
            
            enrollment = [first_name, last_name, father_name, gender, phone_no, address, email, course_teach]
            self.save_teacher(enrollment)
            self.teacher_corner()
   
    def notFound_teacher(self, teacher_id):
        print("    ****** Search Result ******")
        print()

        print(f"Teacher ID : {teacher_id}")
        print("! ! ! Record Not Found ! ! !")
        input("Press any key to go back to last menu")
        u.sleep(1)
        self.search_teacher()

    def delete(self, teacher_id):
        print(f"""
    ****** Delete Menu ******
    
    Teacher ID : {teacher_id}
""")
        print("Are you sure...")
        decision = input("Enter 'y' to delete or 'n' to return.")
        decision = decision.strip().lower()

        match(decision):
            case 'y':
                db.db_delete_teacher(teacher_id)
                print("Record deleted.")
                u.sleep(2)
                self.teacher_corner()

            case 'n':
                self.management_menu(teacher_id)
            
            case _:
                print(" Invalid choice! \n Try again in 3 seconds.")
                u.sleep(3)
                self.delete(teacher_id)

    def show(self, teacher_id):
        rows = db.db_get_teacher(teacher_id)
        
        u.clear_screen()
        if not rows:
            self.notFound_teacher(teacher_id)
            return

        print("    " + "="*145)
        print("    {:^145}".format("TEACHER DETAILS"))
        print("    " + "="*145)
        
        # Define Headers
        headers = ["ID", "First Name", "Last Name", "Father Name", "Gender", "Phone", "Address", "Email", "Course"]
        print(f"    {headers[0]:<5} | {headers[1]:<12} | {headers[2]:<12} | {headers[3]:<15} | {headers[4]:<8} | {headers[5]:<13} | {headers[6]:<25} | {headers[7]:<20} | {headers[8]:<15}")
        print("    " + "-"*145)
        
        for row in rows:
            # row[0]=ID, row[1]=First, row[2]=Last, etc.
            print(f"    {str(row[0]):<5} | {str(row[1]):<12} | {str(row[2]):<12} | {str(row[3]):<15} | {str(row[4]):<8} | {str(row[5]):<13} | {str(row[6]):<25} | {str(row[7]):<20} | {str(row[8]):<15}")
        
        print("    " + "="*145)
        input("\n    Press any key to go back.")
        self.teacher_corner()

    def update(self, t_id):
        u.clear_screen()
        print(f"    ****** Update Teacher (ID: {t_id}) ******")
        print("\n")
        first_name = input("    Enter new First name : ")
        last_name = input("    Enter new Last name : ")
        father_name = input("    Enter new Father name : ")
        gender = input("    Enter new Gender : ")
        phone_no = input("    Enter new Phone no. : ")
        address = input("    Enter new Address : ")
        email = input("    Enter new Email Address : ")
        course_teach = input("    Enter new Course you can teach : ")
            
        update_list = [first_name, last_name, father_name, gender, phone_no, address, email, course_teach]
        
        # <------------------------------------------------------<<<
        db.db_update_teacher(t_id, update_list)
        print("Record Updated.")
        u.sleep(2)
        self.management_menu(t_id)

    def management_menu(self, teacher_id):
        u.clear_screen()
        print(f"""
    ****** Management Menu (ID: {teacher_id}) ******
    
    1. Delete record.
    2. Show records.
    3. Update record 
              
    Press "e" to go back to last menu
""")
        choice = input("Enter your choice: ")

        match(choice):
            case '1':
                self.delete(teacher_id)

            case '2':
                self.show(teacher_id)

            case '3':
                self.update(teacher_id)

            case 'e':
                self.teacher_corner()

            case _:
                print(" Invalid choice! \n Try again in 3 seconds.")
                u.sleep(3)
                self.management_menu(teacher_id)
    
 
    def search_teacher(self):
        u.clear_screen()
        print("    ****** Search Menu ******\n")
        teacher_id = input("Enter Teacher id to search : ")
        
        # <-------------------------------------<<<
        rows = db.db_get_teacher(teacher_id)
        
        if rows: 
            self.management_menu(teacher_id)
        else:
            self.notFound_teacher(teacher_id)
        

    def teacher_corner(self):
        u.clear_screen()
        print("""
    ****** Teachers Corner ******
    
    1. Insert record.
    2. Search record.

    Press "e" to go back to last menu.
""")
        choice = str(input("Enter your choice. "))

        match(choice):
            case '1':
                self.new_teacher()

            case '2':
                self.search_teacher()

            case 'e':
                p = Principal()
                p.main()

            case _:
                print("Invalid choice.")
                u.sleep(3)
                self.teacher_corner()


# ------------------------------------------------------ #


class Record_student():

    def notFound_student(self, student_id):
        print("    ****** Search Result ******")
        print()
        print(f"Student ID : {student_id}")
        print("! ! ! Record Not Found ! ! !")
        input("Press any key to go back to last menu")
        u.sleep(1)
        self.student_corner()

    def search_student(self):
        u.clear_screen()
        print("    ****** Search Menu ******\n")
        student_id = input("Enter Student ID : ")
        
        # <-------------------------------------<<<
        rows = db.db_get_student(student_id)

        if rows: 
            self.management_menu(student_id)
        else:
            self.notFound_student(student_id)
 

    def delete(self, student_id):
        print("    ****** Delete Menu ******\n")
        decision = input("Enter 'y' to delete or 'n' return to last menu.")
        decision = decision.strip().lower()

        match(decision):
            case 'y':
                # <------------------------------------------------------<<<
                db.db_delete_student(student_id)
                print("Student deleted.")
                u.sleep(2)
                self.student_corner()
            
            case 'n':
                self.management_menu(student_id)

    def show_student(self, student_id):
        u.clear_screen()
        student = db.db_get_student(student_id)
        
        if not student:
            self.notFound_student(student_id)
            return

        print("    " + "="*145)
        print("    {:^145}".format("STUDENT DETAILS"))
        print("    " + "="*145)
        
        headers = ["ID", "First Name", "Last Name", "Father Name", "Gender", "Phone", "Address", "Email", "Enrolled"]
        print(f"    {headers[0]:<5} | {headers[1]:<12} | {headers[2]:<12} | {headers[3]:<15} | {headers[4]:<8} | {headers[5]:<13} | {headers[6]:<25} | {headers[7]:<20} | {headers[8]:<15}")
        print("    " + "-"*145)
        
        for row in student:
            print(f"    {str(row[0]):<5} | {str(row[1]):<12} | {str(row[2]):<12} | {str(row[3]):<15} | {str(row[4]):<8} | {str(row[5]):<13} | {str(row[6]):<25} | {str(row[7]):<20} | {str(row[8]):<15}")
        
        print("    " + "="*145)
        input("\n    Press any key to go back.")
        self.management_menu(student_id)

    def update_student(self, student_id):
        u.clear_screen()
        print(f"    ****** Update Student (ID: {student_id}) ******")
        print("\n")
        try:
            first_name = input("    Enter new First name : ")
            last_name = input("    Enter new Last name : ")
            father_name = input("    Enter new Father name : ")
            gender = input("    Enter new Gender : ")
            phone_no = input("    Enter new Phone no. : ")
            address = input("    Enter new Address : ")
            email = input("    Enter new Email Address : ")
            course_to_enroll = input("    Enter new Course to enroll in : ")
                
            enrollment = [first_name, last_name, father_name, gender, phone_no, address, email, course_to_enroll]
            
            # <------------------------------------------------------<<<
            db.db_update_student(student_id, enrollment)
            print("Student Updated.")
            u.sleep(2)

        except Exception as e:
            print("Error : ", e)
            u.sleep(3)
        
        self.management_menu(student_id)

    def management_menu(self, student_id):
        u.clear_screen()
        print(f"""
    ****** Management Menu (ID: {student_id}) ******
    
    1. Delete record.
    2. Show records.
    3. Update record 
              
    Press "e" to go back to last menu
""")
        choice = input("Enter your choice: ")

        match(choice):
            case '1':
                self.delete(student_id)

            case '2':
                self.show_student(student_id)

            case '3':
                self.update_student(student_id)

            case 'e':
                self.student_corner()

            case _:
                print(" Invalid choice! \n Try again in 3 seconds.")
                u.sleep(3)
                self.management_menu(student_id) 

        

    def approval(self):
        u.clear_screen()
        print("    ****** Add New Student ******")
        
        first_name = input("    First name : ")
        last_name = input("    Last name : ")
        father_name = input("    Father name : ")
        gender = input("    Gender : ")
        phone_no = input("    Phone no. : ")
        address = input("    Address : ")
        email = input("    Email Address : ")
        course_enroll = input("    Course to enroll : ")

        data = [first_name, last_name, father_name, gender, phone_no, address, email, course_enroll]
        
        # <------------------------------------------------------<<<
        db.db_add_student(data)
        print("    Student added successfully.")
        u.sleep(2)
        self.student_corner()


    def student_corner(self):
        u.clear_screen()
        print("""
    ****** Students Corner ******
    
    1. Insert record.
    2. Search record.

    Press "e" to go back to last menu.
""")
        choice = str(input("Enter your choice. "))

        match(choice):
            case '1':
                self.approval()

            case '2':
                self.search_student()

            case 'e':
                p = Principal()
                p.main()

            case _:
                print("Invalid choice.")
                u.sleep(3)
                self.student_corner()

# ------------------------------------------------------ #


class Record_courses():

    def check(self, course_id):
        # <------------------------------------------------------<<<
        return db.db_check_course(course_id)

    def delete(self):
        print("    ****** Delete Menu ******")
        delete_course = input("Enter your course id to delete: ")
        # <------------------------------------------------------<<< 
        db.db_delete_course(delete_course)
        print("Course deleted.")
        u.sleep(2)
        self.management_menu()

    def show(self):
        u.clear_screen()
        #           <------------------------------------------------------<<<
        print(f"""
    ****** All Courses ******
    Course ID    |     Course Name   |    Department
""")
        courses = db.db_get_all_courses()
        for course in courses:
            print(f"    {course[0]}  |   {course[1]}   |  {course[2]}")

        input("\n    Press any key to go back to last menu.")
        self.management_menu()


    def management_menu(self):
        u.clear_screen()
        print("""
    ****** Management Menu ******
    
    1. Delete record.
    2. Show records.
              
    Press "e" to go back to last menu
""")
        choice = input("Enter your choice: ")

        match(choice):
            case '1':
                self.delete()

            case '2':
                self.show()

            case 'e':
                self.courses_corner()

            case _:
                print(" Invalid choice! \n Try again in 3 seconds.")
                u.sleep(3)
                self.management_menu()

    def not_recordFound(self, course_id):
        print("    ****** Search Course ******")
        print()
        #           <------------------------------------------------------<<<
        print(f"Course ID : {course_id}")
        print("! ! ! Record Not Found ! ! !")
        input("Press any key to go back to last menu")
        u.sleep(1)
        self.search()

    def save_course(self, new_course_name):
        # <------------------------------------------------------<<<
        db.db_add_course(new_course_name)
        print("Course Saved.")
        u.sleep(1)

    def search(self):
        print("    ****** Search Course ******")
        print()
        course_id = input("Enter your course_id: ")
        found = self.check(course_id)

        if found:
            print("Course Found.")
            u.sleep(1)
            self.management_menu()
        
        else:
            u.clear_screen()
            self.not_recordFound(course_id)

    def new_course(self):
        u.clear_screen()
        print("    ****** Introducing New Course ******")
        print("\n")
        new_course = input("    Enter new course name to add: ")
        self.save_course(new_course)
        self.courses_corner()

    def courses_corner(self):
        u.clear_screen()
        print("""
    ****** Courses Corner ******
    
    1. Insert record.
    2. Search record.

    Press "e" to go back to last menu.
""")
        choice = str(input("Enter your choice. "))

        match(choice):
            case '1':
                self.new_course()

            case '2':
                self.search()

            case 'e':
                p = Principal()
                p.main()

            case _:
                print("Invalid choice.")
                u.sleep(3)
                self.courses_corner()


# ------------------------------------------------------ #


class Principal:
    def main(self):
        u.clear_screen()
        print("""
    ****** Welcome Principal ******

    1. Teachers Corner
    2. Students Corner
    3. Courses Corner

    Press "e" to Exit..
""")
        choice = str(input("Enter your choice: "))
        choice = choice.strip().lower()

        match (choice):
            case '1':
                t = Record_teacher()
                t.teacher_corner()

            case '2':
                s = Record_student()
                s.student_corner()
            
            case '3':
                c = Record_courses()
                c.courses_corner()
            
            case "e":
                print("Exiting.......")
                u.sleep(2)
            
            case _:
                print("Invalid choice.")
                print("Try again in 3 seconds.")
                u.sleep(3)



# ------------------------------------------------------ #



def main():
    u.clear_screen()
    print("""
**** Welcome to Student Management System ****

    1. Principal
    2. Teacher
    3. Student
          
    Press "e" to exit....
""")
    choice = input()
    if choice == 'e':
        print("Exiting....")
        print("Thanks for coming.")
        u.sleep(2)

    else:
        try:
            choice = int(choice)
            match (choice):
                case 1:
                    Login_Signup(1)

                case 2:
                    Login_Signup(2)

                case 3:
                    Login_Signup(3)
        except ValueError:
            main()


# ------------------------------------------------------ #


if __name__ == "__main__":
    main()
