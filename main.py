from time import sleep
from os import system


def clear_screen():
    # <------------------------------------------------------<<<
    _ = system('cls')

def getData(username, password):
    # <------------------------------------------------------<<<
    pass

def save_data(username, email, password):
    # <------------------------------------------------------<<<
    pass

def getEmail():
    # <------------------------------------------------------<<<
    pass

def user_Check(username, password)-> bool:
    
    user, passwd = getData(username, password)
    if(username == user and passwd == password):
        exist = True
    
    else:
        exist = False

    return exist

def email_check(email, username)-> bool:
    mail = getEmail()

    if mail == email:
        return True
    
    else:
        return False


def Login_Signup(num):
    panel = num
    # <------------------------------------------------------<<<
    clear_screen()
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
    clear_screen()
    print("""
    *********** Login ***********
    
    Enter your details:
          
""")
    username = input("    Username: ")
    password = input("    Password: ")
    
    value : bool = user_Check(username, password)

    if value and num == 1:
        obj_principal = Principal()
        obj_principal.main()

    elif value and num == 1:
        obj_teacher = Teacher()
        obj_teacher.main()

    elif value and num == 1:
        obj_student = Student()
        obj_student.main()

def signup(panel):
    while(True):
        clear_screen()
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
            sleep(3)
            return
  

# ------------------------------------------------------ #

    
    
class Record_teacher():

    def save_teacher(self, enrollment):
        # <------------------------------------------------------<<<
        print("Enrollment saved successfully.")

    def new_teacher(self):
            clear_screen()
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
        sleep(1)
        self.search_teacher()

 
    def search_teacher():
        print("    ****** Search Menu ******\n")

        teacher_id = input("Enter Teacher id to search : ")
        

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
                sleep(3)
                self.teacher_corner()


# ------------------------------------------------------ #


class Record_student():
    pass

# ------------------------------------------------------ #


class Record_courses():

    def check(self, course_id):
        # search commands with course_id <------------------------------------------------------<<<
        pass

    def delete(self):
        print("    ****** Show Menu ******")
        delete_course = input("Enter your course id to delete.")
        # delete commands <------------------------------------------------------<<< 
        sleep(2)
        self.management_menu()

    def show(self):
        clear_screen()
        #           <------------------------------------------------------<<<
        print(f"""
    ****** Show Menu ******
    
    Course ID : {course_id}
    Course Name : {course_name}

""")
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
                sleep(3)
                self.management_menu()

    def not_recordFound(self, course_id):
        print("    ****** Search Course ******")
        print()
        #           <------------------------------------------------------<<<
        print(f"Course ID : {course_id}")
        print("! ! ! Record Not Found ! ! !")
        input("Press any key to go back to last menu")
        sleep(1)
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
            clear_screen()
            self.not_recordFound()

    def new_course(self):
        clear_screen()
        print("    ****** Introducing New Course ******")
        print("\n")
        new_course = input("    Enter new course name to add.")
        self.save_course(new_course)
        self.courses_corner()

    def courses_corner(self):
        print("""
    ****** Courses ******
    
    1. Insert course record.
    2. Search course record.

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
                sleep(3)
                self.courses_corner()


# ------------------------------------------------------ #


class Principal:
    def main():
        clear_screen()
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
                t.corner()

            case '2':
                s = Record_student()
                s.corner()
            
            case '3':
                c = Record_courses()
                c.corner()
            
            case "e":
                print("Exiting.......")
                sleep(2)
            
            case _:
                print("Invalid choice.")
                print("Try again in 3 seconds.")
                sleep(3)


# ------------------------------------------------------ #


class Teacher:
    def main():
        clear_screen()


# ------------------------------------------------------ #


class Student:
    def main():
        clear_screen()


# ------------------------------------------------------ #



def main():
    clear_screen()
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
        sleep(2)

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