import mysql.connector
from mysql.connector import Error
import threading
import queue

MAX_POOL_SIZE = 10
connection_pool = queue.Queue(maxsize=MAX_POOL_SIZE)


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


def connect():
    return create_connection()


def query(pool, query_string="SELECT 1;"):
    if pool:
        connection = connection_pool.get(block=True)
    else:
        connection = connect()
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
            if pool:
                connection_pool.put(connection)
            else:
                connection.close()
    else:
        print("Failed to establish a connection")


def parallel_queries(pool, num_connections):
    if pool:
        initialize_connection_pool()
    threads = []
    for _ in range(num_connections):
        thread = threading.Thread(target=query, kwargs={'pool': pool})
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def initialize_connection_pool():
    for _ in range(MAX_POOL_SIZE):
        connection = create_connection()
        if connection:
            connection_pool.put(connection)


def main():
    pool = True
    num_connections = 1000
    parallel_queries(pool, num_connections)


if __name__ == "__main__":
    main()
