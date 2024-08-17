import time
from threading import Thread

import mysql.connector


def get_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='secret',
        database='employee'
    )
    return conn


def basic_query():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()
    for employee in employees:
        print(employee)
    cursor.close()
    conn.close()


def deadlock(first_id, second_id, type):
    print("Enter the method")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM employees where id = {first_id} {type}')
    employee = cursor.fetchone()
    print(f'Fetched first employee: {employee}')
    print("Now let's take a break")
    time.sleep(10)
    print("Break complete")
    cursor.execute(f'SELECT * FROM employees where id = {second_id} {type}')
    employee = cursor.fetchone()
    print(f'Fetched second employee: {employee}')
    cursor.close()
    conn.close()


if __name__ == '__main__':
    # possible types of lock
    # FOR UPDATE, FOR UPDATE NOWAIT, FOR UPDATE SKIP LOCKED
    type = 'FOR UPDATE SKIP LOCKED'
    thread1 = Thread(target=deadlock, kwargs={'first_id': 1, 'second_id': 2, 'type': type})
    thread2 = Thread(target=deadlock, kwargs={'first_id': 2, 'second_id': 1, 'type': type})

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
