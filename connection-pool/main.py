import mysql.connector
from mysql.connector import Error
import threading
from queue import BlockingQueue

from timeit import timeit

MAX_POOL_SIZE = 100
connection_pool = BlockingQueue(maxsize=MAX_POOL_SIZE)


def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="my-secret-pw"
        )
        if connection.is_connected():
            return connection
        else:
            print("Couldn't connect to DB")
            return None
    except Error:
        print("Error while connecting to MySQL")
        return None


def connect(pool):
    if pool:
        return connection_pool.get()
    else:
        return create_connection()


def close(connection, pool):
    if pool:
        connection_pool.put(connection)
    else:
        connection.close()


def query(use_pool, query_string="SELECT 1;"):
    connection = connect(use_pool)
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(query_string)
            record = cursor.fetchone()
            print(f"Result of the dummy query: {record}")
        except Error:
            print("Error while executing query")
        finally:
            cursor.close()
            close(connection, use_pool)
    else:
        print("Failed to establish a connection")


def execute_queries_in_parallel(use_pool, num_connections):
    if use_pool:
        initialize_connection_pool()
    threads = []
    for _ in range(num_connections):
        thread = threading.Thread(target=query, kwargs={'use_pool': use_pool})
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def initialize_connection_pool():
    for _ in range(MAX_POOL_SIZE):
        connection = create_connection()
        if connection:
            connection_pool.put(connection)


@timeit
def main():
    pool = True
    num_connections = 1000
    execute_queries_in_parallel(pool, num_connections)


if __name__ == "__main__":
    main()
