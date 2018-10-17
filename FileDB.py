#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import mysql.connector

config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'port': 8889,
    'database': 'users',
    'raise_on_warnings': True,
}

db = mysql.connector.connect(**config)
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print(data)

# sql = """CREATE TABLE TestTable (
# #         name CHAR(20) NOT NULL,
# #         location CHAR(100),
# #         gender CHAR(1),
# #         age INTEGER )"""

sql = """INSERT INTO TestTable(
name, location, gender, age)
VALUES(
'Maxim', 'EN', 'M', 29)"""

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()
