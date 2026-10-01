import sqlite3
con=sqlite3.connect("company.db")
c=con.cursor()
c.execute("""
    CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    salary INTEGER
    );
""")
def add_employee():
    try:
        name=input("Enter employee name:")
        age=int(input("Enter employee age:"))
        salary=int(input("Enter employee salary:"))
        c.execute("""
            INSERT INTO employees (name,age,salary)VALUES(?,?,?)""",(name,age,salary))
        con.commit()
        print("Employee added")
    except ValueError:
        print("Invalid input.Enter valid input ")
    except Exception as e:
        print(f"Error:{e}")
def view_all_emp():
    c.execute('SELECT * FROM employees')
    for i in c.fetchall():
        print(f"{i[0]}-{i[1]}-Age:{i[2]}-Salary:{i[3]}")
def salary_more():
    c.execute('SELECT * FROM employees WHERE salary >=40000')
    for i in c.fetchall():
        print(f"{i[1]}-{i[3]}")
def avg():
    c.execute('SELECT AVG(salary) FROM employees')
    for i in c.fetchall():
        print(f"Average Salary:{i[0]}")
def search():
    try:
        eid=int(input("Enter employee id:"))
        c.execute('SELECT * FROM employees WHERE id=?',(eid,))
        data=c.fetchone()
        if data:
            print(f"{data[0]}-{data[1]}- Age:{data[2]} - Salary:{data[3]}")
        else:
            print("Not found")
    except ValueError:
        print("Invalid input.Enter valid employee id")
    except Exception as e:
        print(f"Error:{e}")
def delete():
    try:
        eid=int(input("Enter employee id:"))
        c.execute("SELECT id FROM employees WHERE id=?",(eid,))
        d=c.fetchone()
        if d:
            c.execute('DELETE FROM employees WHERE id=?',(eid,))
            con.commit()
            print("Employee deleted")
        else:
            print("Employee not found")
    except ValueError:
        print("Invalid input.Enter valid employee id")
    except Exception as e:
        print(f"Error:{e}")

while True:
    try:
        print("=========EMPLOYEE MANAGEMENT SYSTEM==========")
        print("1.Add Employee\n2.View all Employees\n3.View Employees with salary>=40000\n4.Show average salary\n5.Search Employee\n6.Delete Employee\n7.Exit\n")
        choice=int(input("Enter your choice:"))
        if choice==1:
            add_employee()
        elif choice==2:
            view_all_emp()
        elif choice==3:
            salary_more()
        elif choice==4:
            avg()
        elif choice==5:
            search()
        elif choice==6:
            delete()
        elif choice==7:
            print("You are exited")
            con.close()
            break
        else:
            print("Enter a valid choice")

    except ValueError:
        print("Invalid input.Enter valid input")
    except Exception as e:
        print(f"Error:{e}")