import db_connection

def add_student(values):
    query="""
            INSERT INTO students(register_number,full_name,e_mail,date_of_birth,gender) 
            VALUES(%s,%s,%s,%s,%s)
          """

    conn=db_connection.get_connection()
    cur=conn.cursor()
    cur.execute(query,values)
    conn.commit()

    cur.close()
    conn.close()


def view_student():
    query="""
            SELECT * FROM students;
          """
    conn=db_connection.get_connection()
    cur=conn.cursor()
    cur.execute(query)
    data=cur.fetchall()

    cur.close()
    conn.close()

    return data

def search_student(student_id):
    query="""
           SELECT * FROM students WHERE student_id=%s;
          """
    conn=db_connection.get_connection()
    cur=conn.cursor()
    cur.execute(query,(student_id,))
    data=cur.fetchall()

    cur.close()
    conn.close()
    
    return data

def update_student():
    pass

def delete_student():
    pass

search_student(202)