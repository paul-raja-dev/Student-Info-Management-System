import db_connection

def add_student():
    query="""
            INSERT INTO students(student_id,register_number,full_name,e_mail,date_of_birth,gender) 
            VALUES(%s,%s,%s,%s,%s,%s)
          """
    
    s_id=int(input('Enter the student id : '))
    reg_no=input('Enter the register no : ')
    name=input('Enter the Full Name of the student : ')
    e_mail=input('Enter the E-mail of the student : ')
    dob=input('Enter the DOB in the format YYYY-MM-DD : ')
    gender=input('Enter the Gender of the student(M/F) : ')

    values=(s_id,reg_no,name,e_mail,dob,gender)



    conn=db_connection.get_connection()
    cur=conn.cursor()
    cur.execute(query,values)
    conn.commit()

    cur.close()
    conn.close()
    print('Query run successfully ! ')




add_student()



def view_student():
    pass

def update_student():
    pass

def delete_student():
    pass