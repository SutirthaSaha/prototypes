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
    # First, collect a random subset of potential target nodes 'b'
    potential_targets = tx.run(
        "MATCH (b:Node) "
        "WHERE id(b) <> $start_node_id "
        "RETURN id(b) AS id "
        "ORDER BY rand() "
        "LIMIT $num_relationships",  # Only consider a subset of nodes
        start_node_id=start_node.element_id, num_relationships=num_relationships
    ).value()

    # Now, create relationships to the randomly chosen target nodes
    for target_node_id in potential_targets:
        # Directly match 'a' and 'b' by their IDs to avoid a Cartesian product
        tx.run(
            "MATCH (a:Node) WHERE id(a) = $start_node_id "
            "MATCH (b:Node) WHERE id(b) = $target_node_id "
            "MERGE (a)-[:RELATED]->(b)",  # Use MERGE to avoid creating duplicate relationships
            start_node_id=start_node.element_id, target_node_id=target_node_id
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


def _traverse_graph(tx, depth):
    query = f"""
    MATCH (n:Node)-[*..{depth}]->(m:Node)
    RETURN n.name, m.name
    LIMIT 100
    """
    return tx.run(query).data()


class Neo4j:
    def __init__(self, uri, username, password):
        self.driver = GraphDatabase.driver(uri, auth=(username, password))

    def create_graph(self, num_nodes, num_relationships):
        with self.driver.session() as session:
            for index in range(num_nodes):
                start_node = session.execute_write(_create_node)
                session.execute_write(_create_relationships, start_node, num_relationships)
                if index % 10000 == 0:
                    print(f"Added {index} nodes to the graph")

    def traverse_all_nodes(self):
        with self.driver.session() as session:
            result = session.execute_read(_get_all_nodes)
            return result

    def complex_traversal(self, depth):
        with self.driver.session() as session:
            start_time = time.time()
            result = session.read_transaction(_traverse_graph, depth)
            end_time = time.time()
            print(f"Traversal completed in {end_time - start_time} seconds")
            return result

    def __del__(self):
        self.driver.close()


if __name__ == "__main__":
    db = Neo4j(uri, username, password)
    n, m, depth = 100000, 100000, 20
    db.create_graph(n, m)
    # nodes = db.traverse_all_nodes()
    # for node in nodes:
    #     print(dict(node))
    #
    # result = db.complex_traversal(depth)
    #
    # # Step 3: Output some results (or just measure the performance)
    # print(f"Traversal result: {result}")