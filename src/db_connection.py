from dotenv import load_dotenv
import os
import MySQLdb

load_dotenv()

conn=MySQLdb.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSWORD'),
    db=os.getenv('DB_NAME')
)

cur=conn.cursor()

cur.execute("SHOW TABLES;")
table=cur.fetchall()
for i in table:
    print(i)

cur.close()
conn.close()
