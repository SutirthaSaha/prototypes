from elasticsearch import Elasticsearch
import os


def create_elasticsearch_client():
    # Replace with your actual port-forwarded URL, username, and password
    es_host = os.getenv("URL")
    es_username = os.getenv("USERNAME")
    es_password = os.getenv("PASSWORD")

    # Create an Elasticsearch client
    es = Elasticsearch(
        [es_host],
        basic_auth=(es_username, es_password),
        verify_certs=False,  # Disable SSL certificate verification
        ssl_show_warn=False  # Suppress SSL warnings
    )

    return es
