from neo4j import GraphDatabase
import random
import string
import time

uri = "bolt://localhost:7687"
username = "neo4j"
password = "secret"


def _create_node(tx):
    node_label = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    node = tx.run("CREATE (n:Node {name: $name}) RETURN n", name=node_label)
    return node.single()[0]


def _create_relationships(tx, start_node, num_relationships):
    tx.run(
        "MATCH (a: Node), (b: Node) "
        "WHERE id(a) = $node_id "
        "WITH a, b, rand() AS number "
        "ORDER BY number "
        "LIMIT $num_relationships "
        "CREATE (a)-[:RELATED]->(b)",
        node_id=start_node.id, num_relationships=num_relationships
    )


def _get_all_nodes(tx):
    query = """
    MATCH (n)
    RETURN n
    """
    result = tx.run(query)
    nodes = []
    for record in result:
        nodes.append(record["n"])  # Access the node from the result
    return nodes


class Neo4j:
    def __init__(self, uri, username, password):
        self.driver = GraphDatabase.driver(uri, auth=(username, password))

    def create_graph(self, num_nodes, num_relationships):
        with self.driver.session() as session:
            for _ in range(num_nodes):
                start_node = session.write_transaction(_create_node)
                session.write_transaction(_create_relationships, start_node, num_relationships)

    def traverse_all_nodes(self):
        with self.driver.session() as session:
            result = session.read_transaction(_get_all_nodes)
            return result

    def __del__(self):
        self.driver.close()


if __name__ == "__main__":
    db = Neo4j(uri, username, password)
    n, m = 10000, 500
    db.create_graph(n, m)
    nodes = db.traverse_all_nodes()
    for node in nodes:
        print(dict(node))
