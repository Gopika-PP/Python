import sqlite3
con=sqlite3.connect("school.db")
c=con.cursor()
c.execute("""
    CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    grade INTEGER
          );
""")
def add_student():
    n=input("Enter student name:\n")
    a=input("Enter age:\n")
    g=input("Enter grade:\n")
    c.execute("""INSERT INTO students (name,age,grade)VALUES (?,?,?)""",(n,a,g))
    con.commit()
    print("Student added successfully")
    
def view_all_student():
    c.execute(" SELECT * FROM students ")
    for i in c.fetchall():
        print(f"{i[1]}-Age:{i[2]}-Grade:{i[3]}")

def view_passing_student():
    c.execute(" SELECT * FROM students WHERE grade >=70 ")
    for i in c.fetchall():
        print(f"{i[1]}-Age:{i[2]}-Grade:{i[3]}")

def show_avg_grade():
    c.execute(" SELECT AVG(grade) FROM students")
    for i in c.fetchone():
        print(i)

def search_student():
    sid=input("Enter student id:")
    c.execute(" SELECT * FROM students WHERE id=? ",(sid,))
    d=c.fetchone()
    if d:
        print(f"student-id: {d[0]}     name: {d[1]}     Age:{d[2]}      Grade:{d[3]}")
    else:
        print("Student not found")

def delete_student():
    sid=input("Enter student id:")
    c.execute(" SELECT * FROM students WHERE id=? ", (sid,))
    d = c.fetchone()
    if d:
        c.execute("DELETE FROM students WHERE id=?", (sid,))
        print("Delete Sucessfully")
    else:
        print("Student not found")


while True:
    print("======Student Management System=======\n")
    print("1.Add Student\n2.View All Student\n3.View Passing Students\n4.Show average grade\n5.Search Student\n6.Delete Student\n7.Exit\n")
    choice=int(input("Enter your choice:"))
    if choice==1:
        add_student()
    elif choice==2:
        view_all_student()
    elif choice==3:
        view_passing_student()
    elif choice==4:
        show_avg_grade()
    elif choice==5:
        search_student()
    elif choice==6:
        delete_student()
    elif choice==7:
        con.close()
        exit()
    else:
        print("Invalid choice")

