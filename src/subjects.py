import db_connection

def add_subject(values):
    query="""
          INSERT INTO subjects(subject_code,subject_name,credits)
            VALUES(%s,%s,%s);
        """
    conn=db_connection.get_connection()
    cur=conn.cursor()
    cur.execute(query,(values))
    conn.commit()

    cur.close()
    conn.close()

def view_subject():
    query="""
           SELECT * FROM subjects;
        """
    conn=db_connection.get_connection()
    cur=conn.cursor()
    cur.execute(query)
    data=cur.fetchall()

    cur.close()
    conn.close()
    
    return data

def search_subject(sub_id):
    query="""
           SELECT * FROM subjects WHERE subject_id = %s;
         """
    conn=db_connection.get_connection()
    cur=conn.cursor()
    cur.execute(query,(sub_id,))
    info=cur.fetchall()

    cur.close()
    conn.close()

    return info

def update_subject():
    pass

def delete_subject():
    pass