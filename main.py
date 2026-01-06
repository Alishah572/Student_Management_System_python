from utils import Utils as u
from crypto_utils import generate_key, encrypt_message, decrypt_message
from students import student_management_menu
from teachers import teacher_management_menu

# chars, key = generate_key()

# print("Key:", key)

# # Encryption
# plain_text = input("Enter a message to encrypt: ")
# cipher_text = encrypt_message(plain_text, chars, key)

# print(f"Original message : {plain_text}")
# print(f"Encrypted message : {cipher_text}")

# # Decryption
# cipher_input = input("Enter a message to decrypt: ")
# decrypted_text = decrypt_message(cipher_input, chars, key)

# print(f"Cipher Text : {cipher_input}")
# print(f"Original Message : {decrypted_text}")

def getData(username, password):
    # <------------------------------------------------------<<<
    return

def save_data(username, email, password):
    # <------------------------------------------------------<<<
    return

def user_Check(username, password)-> bool:
    exist = True
    # user, passwd = getData(username, password)
    # if(username == user and passwd == password):
    #     exist = True
    
    # else:
    #     exist = False

    return exist

def email_check(email, username)-> bool:
    # <------------------------------------------------------<<<
    # # mail = list(email)
    # if mail == email:
    #     return True
    
    # else:
    #     return False
    return True


def Login_Signup(num):
    panel = num
    # <------------------------------------------------------<<<
    u.clear_screen()
    print("""
    **** Welcome to login & signup ****
        
        1. Login
        2. Signup
    
    Enter any key to go back to main menu.
""")
    choice = str(input("Enter your choice. "))

    match (choice.strip()):
        case '1':
            login(panel)
        
        case '2':
            signup(panel)
        
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
        print("teach")
        teacher_management_menu()

    if value and num == 3:
        print("student")
        student_management_menu()

    if value and num == 1:
        obj_principal = Principal()
        obj_principal.main()

def signup(panel):
    while(True):
        u.clear_screen()
        print("""
        *********** Login ***********
        
        Enter your details:
            
    """)
        username = input("    Username: ")
        email = input("    Email: ")
        password = input("    Password: ")

        emailCheck = email_check(email, username)
        
        if emailCheck:
            save_data(username,email,password)
            login(panel)

        else:
            print("Invalid Email Address.")
            print("Enter valid email address")
            u.sleep(3)
            return
  

# ------------------------------------------------------ #

    
    
class Record_teacher():

    def save_teacher(self, enrollment):
        # <------------------------------------------------------<<<
        print("Enrollment saved successfully.")

    def new_teacher(self):
            u.clear_screen()
            print("    ****** Introducing New Teacher ******")
            print("\n")
            first_name = input("    First name : ")
            last_name = input("    Last name : ")
            father_name = input("    Father name : ")
            gender = input("    Gender : ")
            phone_no = int(input("    Phone no. : "))
            address = input("    Address : ")
            email = input("    Email Address : ")
            course_teach = input("    Course you can teach : ")
            
            enrollment = [first_name, last_name, father_name, gender, phone_no, address, email, course_teach]
            self.save_teacher(enrollment)
            self.teacher_corner()
   
    def notFound_teacher(self, teacher_id):
        print("    ****** Search Course ******")
        print()
        #           <------------------------------------------------------<<<
        print(f"Course ID : {teacher_id}")
        print("! ! ! Record Not Found ! ! !")
        input("Press any key to go back to last menu")
        u.sleep(1)
        self.search_teacher()

    def delete(self, teacher_id):
        print(f"""
    ****** Delete Menu ******
    
    Teacher ID : {teacher_id}
""")
        # fetch record of this teacher id and display
        print("Are you sure...")
        decision = input("Enter 'y' to delete or 'n' to return.")
        decision = decision.strip().lower()

        match(decision):
            case 'y':
                # database query to delete <------------------------------------------------------<<<
                pass

            case 'n':
                self.management_menu("")
            
            case _:
                print(" Invalid choice! \n Try again in 3 seconds.")
                u.sleep(3)
                self.delete(teacher_id)

    def show(self, teacher_id):
        # data to fetch from database and return a list where id == teacher_id.
        u.clear_screen()
        print("    ****** Teacher's Data ******")
        print("\n")
        print("    ID   |        First_name       |     Last_name        |      Father_name      | Gender |         Phone_no        |       Address      |            Email          |    Course_teaches  |")
        # teacher is the 2D_list return by the database
        for row in teacher:
            print(f"    {row[0]}   |   {row[1]}   |   {row[2]}   |   {row[3]}   |   {row[4]}   |   {row[5]}   |   {row[6]}   |   {row[7]}   |   {row[8]}   |")

        input("Press any key to go back student menu.")
        self.teacher_corner()

    def update(self, t_id):
        u.clear_screen()
        print("    ****** Update Teacher ******")
        print("\n")
        first_name = input("    Enter new First name : ")
        last_name = input("    Enter new Last name : ")
        father_name = input("    Enter new Father name : ")
        gender = input("    Enter new Gender : ")
        phone_no = int(input("    Enter new Phone no. : "))
        address = input("    Enter new Address : ")
        email = input("    Enter new Email Address : ")
        course_teach = input("    Enter new Course you can teach : ")
            
        update_list = [first_name, last_name, father_name, gender, phone_no, address, email, course_teach]
        # Alter Query to update teacher record where teacher_id == t_id
        self.management_menu("")

    def management_menu(self, teacher_id):
        print("""
    ****** Management Menu ******
    
    1. Delete record.
    2. Show records.
    3. Update record 
              
    Press "e" to go back to last menu
""")
        choice = input("Enter your choice")

        match(choice):
            case '1':
                self.delete(teacher_id)

            case '2':
                self.show(teacher_id)

            case '3':
                self.update(teacher_id)

            case 'e':
                self.management_menu(teacher_id)

            case _:
                print(" Invalid choice! \n Try again in 3 seconds.")
                u.sleep(3)
                self.management_menu()
    
 
    def search_teacher(self):
        print("    ****** Search Menu ******\n")

        teacher_id = input("Enter Teacher id to search : ")
        # Check student id in db <-------------------------------------<<<
        # if found in db found = true else false
        # found = teacher_id_exists() # returns true/false

        # if found: 
        self.management_menu(teacher_id)
        
        # else:
        #     self.notFound_teacher(teacher_id)
        

    def teacher_corner(self):
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
                print("Please try again in 3 seconds.")
                u.sleep(3)
                self.teacher_corner()


# ------------------------------------------------------ #


class Record_student():

    def notFound_student(self, student_id):
        print("    ****** Search Course ******")
        print()
        print(f"Course ID : {student_id}")
        print("! ! ! Record Not Found ! ! !")
        input("Press any key to go back to last menu")
        u.sleep(1)
        self.student_corner()

    def search_student(self):
        u.clear_screen()
        print("""
    ****** Search Menu ******

""")
        student_id = input("Enter Student ID : ")
        # Check student id in db <-------------------------------------<<<
        # if found in db found = true else false
        found = student_id_exists() # returns true/false

        if found: 
            self.management_menu(student_id)
        
        else:
            self.notFound_student(student_id)
 

    def delete(self, student_id):
        print("    ****** Delete Menu ******\n")
        decision = input("Enter 'y' to delete or 'n' return to last menu.")
        decision = decision.strip().lower()

        match(decision):
            case 'y':
                # delete record from the database
                self.student_corner()
            
            case 'n':
                self.management_menu(student_id)

    def show_student(self, student_id):
        # data to fetch from database and return a list where id == student_id.
        u.clear_screen()
        print("    ****** Student's Data ******")
        print("\n")
        print("    ID   |        First_name       |     Last_name        |      Father_name      | Gender |         Phone_no        |       Address      |            Email          |    Course enrolled in  |")
        # student is the 2D_list return by the database
        for row in student:
            print(f"    {row[0]}   |   {row[1]}   |   {row[2]}   |   {row[3]}   |   {row[4]}   |   {row[5]}   |   {row[6]}   |   {row[7]}   |   {row[8]}   |")

    def update_student(self, student_id):
        u.clear_screen()
        print("    ****** Update Teacher ******")
        print("\n")
        try:
            first_name = input("    Enter new First name : ")
            last_name = input("    Enter new Last name : ")
            father_name = input("    Enter new Father name : ")
            gender = input("    Enter new Gender : ")
            phone_no = int(input("    Enter new Phone no. : "))
            address = input("    Enter new Address : ")
            email = input("    Enter new Email Address : ")
            course_to_enroll = input("    Enter new Course to enroll in : ")
                
            enrollment = [first_name, last_name, father_name, gender, phone_no, address, email, course_to_enroll]
        except Exception as e:
            print("Error : ", e)
        # Alter Query to update teacher record where teacher_id == t_id
        self.management_menu("")

    def management_menu(self, student_id):
        print("""
    ****** Management Menu ******
    
    1. Delete record.
    2. Show records.
    3. Update record 
              
    Press "e" to go back to last menu
""")
        choice = input("Enter your choice")

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
                self.management_menu() 

        

    def approval(self):
        u.clear_screen()
        print("    ****** Approval Menu ******")
        self.show() # Ahmad raza your function for json data to show

        approve_permission = input("    1. Approve admission\n    2. Reject admission")
        if approve_permission:
            for row in data: # json data to feed in sql database (Farhan your function)
                database_row : list = row
            # Email notification for approval

        else:
            print("The application has been rejected.")
            # email notification for rejection
            print("Better luck next time.")
            u.sleep(3)
            self.student_corner()

    def student_corner(self):
        print("""
    ****** Courses ******
    
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
                print("Please try again in 3 seconds.")
                u.sleep(3)
                self.student_corner()

# ------------------------------------------------------ #


class Record_courses():

    def check(self, course_id):
        # search commands with course_id <------------------------------------------------------<<<
        pass

    def delete(self):
        print("    ****** Show Menu ******")
        delete_course = input("Enter your course id to delete.")
        # delete commands <------------------------------------------------------<<< 
        u.sleep(2)
        self.management_menu()

    def show(self):
        u.clear_screen()
        #           <------------------------------------------------------<<<
        print(f"""
    ****** Show Menu ******
    Course ID    |     Course Name   |    Department
""")
        for course in courses:
            print(f"    {course[0]}  |   {course[1]}   |  {course[2]}")

        input(    "Press any key to go back to last menu.")
        self.management_menu()


    def management_menu(self):
        print("""
    ****** Management Menu ******
    
    1. Delete record.
    2. Show records.
              
    Press "e" to go back to last menu
""")
        choice = input("Enter your choice")

        match(choice):
            case '1':
                self.delete()

            case '2':
                self.show()

            case 'e':
                self.search()

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

    def save_course(self, new_course):
        # <------------------------------------------------------<<<
        pass

    def search(self):
        print("    ****** Search Course ******")
        print()
        course_id = int(input("Enter your course_id"))
        found = self.check(course_id)

        if found:
            self.management_menu()
        
        else:
            u.clear_screen()
            self.not_recordFound()

    def new_course(self):
        u.clear_screen()
        print("    ****** Introducing New Course ******")
        print("\n")
        new_course = input("    Enter new course name to add.")
        self.save_course(new_course)
        self.courses_corner()

    def courses_corner(self):
        print("""
    ****** Courses ******
    
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
                print("Please try again in 3 seconds.")
                u.sleep(3)
                self.courses_corner()


# ------------------------------------------------------ #


class Principal:
    def main(self):
        u.clear_screen()
        print("""
    ****** Welcome ******

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
        choice = int(choice)
        match (choice):
            case 1:
                Login_Signup(1)

            case 2:
                Login_Signup(2)

            case 3:
                Login_Signup(3)


# ------------------------------------------------------ #


if __name__ == "__main__":
    main()

