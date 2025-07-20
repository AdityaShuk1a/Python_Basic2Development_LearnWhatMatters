import sqlite3

conn = sqlite3.connect("EmployeeDB")

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS employee(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               age INTEGER,
               department TEXT,
               salary INTEGER
               )

''')

conn.commit()

def add_employee():

    name = input("Enter name: ")
    age  = int(input("Enter employee age: "))
    department = input("Enter department")
    salary = int(input("Enter employee salary: "))

    cursor.execute('''
        INSERT INTO employee (name, age, department, salary) values (?, ?, ?, ?)
''', (name, age, department, salary))
    
    conn.commit()
    print("employee data has been inserted")

def view_employee():

    cursor.execute('''
    SELECT * FROM employee
''')
    
    rows = cursor.fetchall()
    print("All employees")
    for row in rows:
        print(row)

def search_employee():
    emp_id = int(input("Enter employee id: "))
    cursor.execute('''
    SELECT * FROM employee WHERE id = ?
''', (emp_id,  ))
    
    row = cursor.fetchone()
    if row:
        print(row)
    else:
        print("employee does not exists")

def update_employee():
    emp_id = int(input("Enter employee id: "))

    cursor.execute("SELECT * FROM employee WHERE id = ?", (emp_id, ))

    employee = cursor.fetchone()

    if employee:

        print("Enter user details: \n")
        name = input("Enter employee new name: ")
        age = int(input("Enter employee new age: "))
        department = input("Enter employee new department: ")
        salary = int(input("Enter employee new salary: "))

        cursor.execute('''
        UPDATE employee SET name = ?, age = ?, department = ?, salary = ? WHERE id = ?
''',     (name, age, department, salary, emp_id))

        conn.commit()

        print("Employee details has been updated")
    else:
        print("Employee does not exists")


def delete_employee():

    emp_id = int(input("Enter employee id: "))

    cursor.execute("SELECT * FROM employee WHERE id = ?", (emp_id, ))

    employee = cursor.fetchone()

    if employee:

        cursor.execute("DELETE FROM employee WHERE id = ?", (emp_id, ))
        print("Employee data has been deleted")
        conn.commit()
    else:
        print("Employee does not exists")



def menu():
    print("Welcome to Employee Management System")
    print("Choice 1 is Add new Employee")
    print("Choice 2 is View Employees")
    print("Choice 3 is Search Employee")
    print("Choice 4 is Update Employee")
    print("Choice 5 is Delete Employee")
    print("Choice other than these exit the System")


    while True:

        choice = int(input("Enter choice: "))

        if choice == 1 :
            add_employee()
        elif choice == 2:
            view_employee()
        elif choice == 3:
            search_employee()
        elif choice == 4:
            update_employee()
        elif choice == 5:
            delete_employee()
        else:
            print("System closed")
            break



if __name__ == '__main__':
    menu()
    conn.close()