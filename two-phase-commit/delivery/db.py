import mysql.connector
from mysql.connector import Error

from contextlib import contextmanager


@contextmanager
def begin_transaction(connection):
    try:
        # Start transaction
        connection.start_transaction()
        yield
        # Commit transaction
        connection.commit()
    except Error as e:
        # Rollback transaction in case of error
        connection.rollback()
        raise e


class DB:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='secret',
            database='zomato'
        )

    def reserve_delivery_agent(self):
        with begin_transaction(self.conn):
            cursor = self.conn.cursor
            available_agent_query = "SELECT id from agent where order_id is NULL and is_reserved = 0 FOR UPDATE"
            cursor.execute(available_agent_query)
            agent = cursor.fetchone()

            if agent is None:
                raise ValueError("No free agents")

            agent_id = agent[0]
            reserve_agent_query = "UPDATE agent set is_reserved = 1 where id = %s"
            cursor.execute(reserve_agent_query, (agent_id,))
            cursor.close()
            return agent_id

    def book_delivery_agent(self, agent_id, order_id):
        with begin_transaction(self.conn):
            cursor = self.conn.cursor
            book_agent_query = "UPDATE agent set is_reserved = 0, order_id = %s where id = %s"
            cursor.execute(book_agent_query, (order_id, agent_id,))
            cursor.close()
            return agent_id

