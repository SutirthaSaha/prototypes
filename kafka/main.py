from admin import create_topic
from consumer import consume_messages
from producer import produce_message

if __name__ == '__main__':
    create_topic('localhost:29092', 'test_topic', 3, 1)
    produce_message('localhost:29092', 'test_topic', 'Hello, Kafka!')
    consume_messages('localhost:29092', 'my_group', 'test_topic')
