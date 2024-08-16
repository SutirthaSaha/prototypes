from confluent_kafka import Producer


def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")


def produce_message(bootstrap_servers, topic_name, message):
    producer = Producer({'bootstrap.servers': bootstrap_servers})

    producer.produce(topic_name, value=message, callback=delivery_report)
    producer.flush()
