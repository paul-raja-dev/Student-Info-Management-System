import db_connection
import MySQLdb

def add_marks(values):
    query="""
           INSERT INTO marks(student_id,subject_id,marks,grade)
             VALUES (%s,%s,%s,%s);
         """
    conn=db_connection.get_connection()
    cur=conn.cursor()
    cur.execute(query,(values))
    conn.commit()

    cur.close()
    conn.close()

def view_marks():
    query="""
           SELECT * FROM marks;
        """
    conn=db_connection.get_connection()
    cur=conn.cursor()
    cur.execute(query)
    data=cur.fetchall()

    cur.close()
    conn.close()

    return data

def search_student_s_id(stduent_id):
    query="""
           SELECT * FROM marks WHERE student_id = %s ;
        """
    conn=db_connection.get_connection()
    cur=conn.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(query,(stduent_id,))
    info=cur.fetchall()

    cur.close()
    conn.close()

    return info

def search_by_sub_id(sub_id):
    query="""
           SELECT * FROM marks WHERE subject_id = %s ;
       """
    conn=db_connection.get_connection()
    cur=conn.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(query,(sub_id,))
    info=cur.fetchall()

    cur.close()
    conn.close()

    return info


def delete_student(student_id):
    query="""
           DELETE FROM marks WHERE student_id = %s ;
        """
    conn=db_connection.get_connection()
    cur=conn.cursor()
    cur.execute(query,(student_id,))
    conn.commit()

    cur.close()
    conn.close()

