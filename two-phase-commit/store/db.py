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

    def reserve_food_packet(self, food_id):
        with begin_transaction(self.conn):
            cursor = self.conn.cursor()
            available_packet_query = "SELECT id from packet where order_id is NULL and is_reserved = 0 and food_id = %s"
            cursor.execute(available_packet_query, (food_id,))
            packet = cursor.fetchone()

            if packet is None:
                raise ValueError("No packets left")

            packet_id = packet[0]
            reserve_packet_query = "UPDATE packet set is_reserved = 1 where id = %s"
            cursor.execute(reserve_packet_query, (packet_id,))
            cursor.close()
            return packet_id

    def book_food_packet(self, packet_id, order_id):
        with begin_transaction(self.conn):
            cursor = self.conn.cursor()
            book_packet_query = "UPDATE packet set is_reserved = 0, order_id = %s where id = %s"
            cursor.execute(book_packet_query, (order_id, packet_id,))
            cursor.close()
            return packet_id
