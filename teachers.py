from utils import Utils as u

def teacher_management_menu():
        u.clear_screen()
        print("""
    ****** Management Menu ******
    
    1. Show Teachers.
    2. New Addmission.
              
    Press "e" to exit.
""")
        choice = input("Enter your choice")

        match(choice):
            case '1':
                show_teachers()

            case '2':
                new_addmission()

            case 'e':
                print("Exiting....")
                u.sleep(2)

            case _:
                print(" Invalid choice! \n Try again in 3 seconds.")
                u.sleep(3)
                teacher_management_menu()

def show_teachers():

    print("    ****** Teacher's Data ******")
    path = r'C:\Users\mueed\OneDrive\All About Python\Python\Student_Management_System_python\studentdb.mdf'

    with open(path, 'r') as f:  #  these two line is an example for fetch
        teachers = f.read()     #  data from db and returns a students list
        for teacher in teachers:
                    #  name(first+last)   father_name       gender              phone_no            course_teaches
            print(f"   {teacher[1]}  |   {teacher[2]}   |   {teacher[3]}   |   {teacher[4]}   |   {teacher[5]}   |")

    input("Press any key to go back to last menu.")
    teacher_management_menu()

def approval(addmission_form):
    # Ahmad raza here you will save the above data into json file.
    pass

def new_addmission():
    print("    ****** Addmission Form ******")

    first_name = input("Enter your first name : ")
    last_name = input("Enter your first name : ") 
    father_name = input("Enter your first name : ") 
    gender = input("Enter your first name : ") 
    phone_no = input("Enter your first name : ") 
    address = input("Enter your first name : ")    
    email = input("Enter your first name : ") 
    course_enroll = input("Enter your first name : ") 

    addmission_form = [first_name, last_name, father_name, gender, phone_no, address, email, course_enroll]
    
    print("""
    1. Send for approval
    2. Enter "e" to go back to last menu.
""")
    
    choice = input("Enter your choice.")

    match (choice):
        case 1:
            approval(addmission_form)
            teacher_management_menu()

        case 2:
            teacher_management_menu()

        case _:
            print(" Invalid choice! \n Try again in 3 seconds.")
            u.sleep(3)
            teacher_management_menu()