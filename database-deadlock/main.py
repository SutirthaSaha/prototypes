import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='secret',
    database='employee'
)


def basic_query():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()
    for employee in employees:
        print(employee)
    cursor.close()
