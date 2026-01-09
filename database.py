import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="school_db"
        )
    except Error as e:
        print("DB Error:", e)
        return None

# <------------------------------------------------------<<< AUTH
def db_save_user(username, email, encrypted_pass, key_str, role_id):
    con = create_connection()
    if not con: return False
    
    # Timestamps are automatic
    query = """INSERT INTO auth (user_name, email, password_hash, encryption_key, role_id) 
               VALUES (%s, %s, %s, %s, %s)"""
    try:
        cur = con.cursor()
        cur.execute(query, (username, email, encrypted_pass, key_str, role_id))
        con.commit()
        cur.close()
        con.close()
        return True
    except Error as e:
        print(f"Error saving user: {e}")
        return False

def db_get_user_credentials(username):
    con = create_connection()
    if not con: return None
    # Fetch password info to verify login
    query = "SELECT password_hash, encryption_key, role_id FROM auth WHERE user_name = %s"
    cur = con.cursor()
    cur.execute(query, (username,))
    row = cur.fetchone()
    cur.close()
    con.close()
    return row

def db_email_exists(email):
    con = create_connection()
    if not con: return False
    cur = con.cursor()
    cur.execute("SELECT auth_id FROM auth WHERE email = %s", (email,))
    row = cur.fetchone()
    cur.close()
    con.close()
    return row is not None

# <------------------------------------------------------<<< TEACHERS
def db_add_teacher(data_list):
    con = create_connection()
    if not con: return
    
    query = """INSERT INTO teachers 
               (first_name, last_name, father_name, gender, phone_no, address, email, course_teach) 
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    cur = con.cursor()
    cur.execute(query, tuple(data_list))
    con.commit()
    cur.close()
    con.close()

def db_get_teacher(teacher_id):
    con = create_connection()
    if not con: return []
    cur = con.cursor()
    cur.execute("SELECT * FROM teachers WHERE teacher_id = %s", (teacher_id,))
    row = cur.fetchone()
    cur.close()
    con.close()
    return [row] if row else []

def db_delete_teacher(teacher_id):
    con = create_connection()
    if not con: return
    cur = con.cursor()
    cur.execute("DELETE FROM teachers WHERE teacher_id = %s", (teacher_id,))
    con.commit()
    cur.close()
    con.close()

def db_update_teacher(teacher_id, data_list):
    con = create_connection()
    if not con: return
    # Timestamps will update automatically due to ON UPDATE CURRENT_TIMESTAMP
    query = """UPDATE teachers SET 
               first_name=%s, last_name=%s, father_name=%s, gender=%s, 
               phone_no=%s, address=%s, email=%s, course_teach=%s 
               WHERE teacher_id=%s"""
    params = tuple(data_list) + (teacher_id,)
    cur = con.cursor()
    cur.execute(query, params)
    con.commit()
    cur.close()
    con.close()

# <------------------------------------------------------<<< STUDENTS
def db_add_student(data_list):
    con = create_connection()
    if not con: return
    query = """INSERT INTO students 
               (first_name, last_name, father_name, gender, phone_no, address, email, course_enrolled) 
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    cur = con.cursor()
    cur.execute(query, tuple(data_list))
    con.commit()
    cur.close()
    con.close()

def db_get_student(student_id):
    con = create_connection()
    if not con: return []
    cur = con.cursor()
    cur.execute("SELECT * FROM students WHERE student_id = %s", (student_id,))
    row = cur.fetchone()
    cur.close()
    con.close()
    return [row] if row else []

def db_delete_student(student_id):
    con = create_connection()
    if not con: return
    cur = con.cursor()
    cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    con.commit()
    cur.close()
    con.close()

def db_update_student(student_id, data_list):
    con = create_connection()
    if not con: return
    query = """UPDATE students SET 
               first_name=%s, last_name=%s, father_name=%s, gender=%s, 
               phone_no=%s, address=%s, email=%s, course_enrolled=%s 
               WHERE student_id=%s"""
    params = tuple(data_list) + (student_id,)
    cur = con.cursor()
    cur.execute(query, params)
    con.commit()
    cur.close()
    con.close()

# <------------------------------------------------------<<< COURSES
def db_add_course(course_name):
    con = create_connection()
    if not con: return
    query = "INSERT INTO courses (course_name, department, room_name) VALUES (%s, 'General', 'TBD')"
    cur = con.cursor()
    cur.execute(query, (course_name,))
    con.commit()
    cur.close()
    con.close()

def db_check_course(course_id):
    con = create_connection()
    if not con: return False
    cur = con.cursor()
    cur.execute("SELECT course_id FROM courses WHERE course_id = %s", (course_id,))
    row = cur.fetchone()
    cur.close()
    con.close()
    return row is not None

def db_get_all_courses():
    con = create_connection()
    if not con: return []
    cur = con.cursor()
    cur.execute("SELECT course_id, course_name, department FROM courses")
    rows = cur.fetchall()
    cur.close()
    con.close()
    return rows

def db_delete_course(course_id):
    con = create_connection()
    if not con: return
    cur = con.cursor()
    cur.execute("DELETE FROM courses WHERE course_id = %s", (course_id,))
    con.commit()
    cur.close()
    con.close()