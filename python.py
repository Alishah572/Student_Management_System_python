from time import sleep
from os import system
import mysql.connector
from mysql.connector import Error


def clear_screen():
    _ = system('cls')

def get_connection(query):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="school_db"
    )
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    connection.close()

    if result:
        return result
    return None, None

def getData():
    query = "SELECT password, password FROM auth LIMIT 1"
    connection = get_connection(query)
    return connection

def save_data(username, email, password, hash_key):
    try:

        query = """

                INSERT INTO auth (username, email, password, hash_key)
                VALUES (%s, %s, %s, %s)
            """
        if connection.is_connected():
            connection = get_connection(query)

            cursor = connection.cursor()
            cursor.execute(query, (username, email, password, hash_key))
            connection.commit()

            print("Data saved successfully!")

    except Error as e:
        print("Error while connecting to MySQL:", e)

    finally:
        if get_connection.is_connected():
            cursor.close()
            get_connection.close()

def getEmail():
    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT email FROM auth LIMIT 1"
    cursor.execute(query)

    result = cursor.fetchone()

    cursor.close()
    connection.close()

    if result:
        return result[0]
    return None


def user_Check(username, password)-> bool:
    
    user, passwd = getData()
    if(username == user and passwd == password):
        exist = True
    
    else:
        exist = False

    return exist

def email_check(email)-> bool:
    mail = getEmail()

    if mail == email:
        return True
    
    else:
        return False


def Login_Signup(num):
    panel = num
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
    clear_screen()
    print("""
    *********** Login ***********
    
    Enter your details:
          
""")
    username = input("    Username: ")
    email = input("    Email: ")
    password = input("    Password: ")

    emailCheck = email_check(email)
    
    if emailCheck:
        save_data(username,email,password)
        login(panel)
class Record_teacher():
    pass

class Record_student():
    pass

class Record_courses():
    def search():
        pass
    
    def new_course():
        pass

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

class Teacher:
    def main():
        clear_screen()

class Student:
    def main():
        clear_screen()


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

if __name__ == "__main__":
    main()