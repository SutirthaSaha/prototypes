from confluent_kafka.admin import AdminClient, NewTopic


def create_topic(bootstrap_servers, topic_name, num_partitions, replication_factor):
    admin_client = AdminClient({'bootstrap.servers': bootstrap_servers})

    topic_list = [NewTopic(topic_name, num_partitions=num_partitions, replication_factor=replication_factor)]
    future = admin_client.create_topics(topic_list)

    for topic, f in future.items():
        try:
            f.result()  # The result itself is None
            print(f"Topic '{topic}' created successfully")
        except Exception as e:
            print(f"Failed to create topic '{topic}': {e}")
