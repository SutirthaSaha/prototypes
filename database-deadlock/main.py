import mysql.connector

# connect to the database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='secret',
    database='employee'
)


def basic_query():
    # create a cursor object
    cursor = conn.cursor()
    # execute a query
    cursor.execute('SELECT * FROM employees')
    # fetch all rows from the last executed statement
    employees = cursor.fetchall()
    # iterate through the result
    for employee in employees:
        print(employee)
    # close the connection
    cursor.close()
