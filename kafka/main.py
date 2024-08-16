from admin import create_topic
from consumer import consume_messages
from producer import produce_message

port = '9094'

if __name__ == '__main__':
    create_topic(f'localhost:{port}', 'test_topic', 3, 1)
    produce_message(f'localhost:{port}', 'test_topic', 'Hello, Kafka!')
    consume_messages(f'localhost:{port}', 'my_group', 'test_topic')
