from dotenv import load_dotenv
import os
import MySQLdb

load_dotenv()

def get_connection():
    try:
        conn=MySQLdb.connect(
           host=os.getenv('DB_HOST'),
           user=os.getenv('DB_USER'),
           passwd=os.getenv('DB_PASSWORD'),
           db=os.getenv('DB_NAME')
        )
        return conn
        
    except Exception as e:
        print('Error connecting with the Database',e)
        return None
 
