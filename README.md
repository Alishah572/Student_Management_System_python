📘 Student Record Management System
(Python Console Application – Agile Development)
________________________________________
📌 Project Overview
The Student Record Management System (SRMS) is a Python-based console application designed to manage and maintain student records efficiently.
It automates basic record-handling operations such as insertion, deletion, searching, and displaying student data.
This project is developed for educational purposes and follows an Agile development approach, allowing incremental enhancement and feature expansion.
________________________________________
🎯 Purpose
•	Educational / Learning
•	Practice Python programming fundamentals
•	Implement CRUD operations
•	Understand data validation and exception handling
•	Prepare foundation for database-driven applications
________________________________________
🧾 What is a Student Record Management System?
A Student Record Management System enables educational institutions to store, track, and retrieve student information digitally.
The system manages data such as:
•	Student personal information
•	Course enrollment
•	Academic performance
The application allows authorized users to manage records efficiently through a command-line interface.
________________________________________
⭐ Features
•	Easy insertion of student records
•	Fast searching using roll number
•	Secure deletion of records
•	Display all stored records
•	User-friendly console interaction
•	Scalable design for future database integration
________________________________________
✅ Benefits
•	Eliminates manual record handling
•	Reduces data redundancy
•	Improves accuracy
•	Quick data retrieval
•	Simple and lightweight execution
________________________________________
🛠️ Functional Requirements
The system must support the following operations:
1.	Insert Student Record
2.	Delete Student Record
3.	Show Student Records
4.	Search Student Record
________________________________________
📋 Student Record Structure
Each student record contains:
•	Name of Student
•	Roll Number (Unique Identifier)
•	Course Enrolled
•	Total Marks
________________________________________
🧠 System Approach (Python Console-Based)
The system stores student records using Python data structures such as:
•	Dictionary (preferred, using roll number as key)
•	or List of Dictionaries
1️ Check Record
•	Before inserting a new record, the system checks whether the roll number already exists
•	Prevents duplicate student entries
2️ Create Record
•	Accepts user input from the console
•	Stores data in memory
•	Roll number acts as the primary key
3️ Search Record
•	Searches records using roll number
•	Displays full student details if found
4️ Delete Record
•	Deletes a record using roll number
•	Displays appropriate message if record does not exist
5️ Show Record
•	Displays all stored student records in a formatted manner
________________________________________
⚠️ Exception Handling
The application handles the following cases:
•	Duplicate roll number insertion
•	Searching for a non-existing student
•	Deleting a non-existing record
•	Invalid data input (non-numeric roll number / marks)
•	Empty record list handling
Key Constraints:
•	Roll number must be unique
•	Roll number must be numeric
•	Marks must be numeric and valid
________________________________________
🔒 Non-Functional Requirements
1️ Database Structure
•	Currently uses in-memory storage
•	Designed to support future SQL database integration
2️ Email Sending
•	Placeholder for future email notifications
•	Can be implemented using smtplib in Python
3️ Authentication & Authorization
•	Planned feature
•	Role-based access (Admin, Teacher, Student, Parent)
4️ User Panels
•	Console-based interaction
•	Future scope for:
o	Admin panel
o	Student panel
o	Teacher panel
5️ SQL Database
•	Future enhancement using:
o	MySQL / SQLite / PostgreSQL
•	CRUD operations mapped to database queries
6️ Email Validation
•	Email format validation planned
•	Prevents invalid email entries
________________________________________
🚀 Development Methodology
•	Agile Development
•	Iterative feature addition
•	Continuous testing
•	Incremental improvements
________________________________________
🧪 Future Enhancements
•	Persistent storage using SQL
•	File handling (CSV / JSON)
•	Authentication system
•	Email notifications
•	GUI or Web-based interface
•	REST API integration
________________________________________
👨‍🎓 Educational Outcome
This project helps learners understand:
•	Python console application development
•	Data handling using dictionaries
•	Input validation and exception handling
•	Software requirement analysis
•	Agile development practices
________________________________________
📜 License
This project is developed strictly for educational purposes.
