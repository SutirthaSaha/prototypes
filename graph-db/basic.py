from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
user = "neo4j"
password = "secret"

driver = GraphDatabase.driver(uri, auth=(user, password))


def create_person_node(tx, name):
    tx.run("CREATE (p:Person {name: $name})", name=name)


with driver.session() as session:
    session.write_transaction(create_person_node, "Alice")
    print("Created a person node with the name 'Alice'")

driver.close()

'''
After you run the script, you can check if the node was created by going to your browser and accessing:

http://localhost:7474  
 
Use the Neo4j Browser to run the Cypher query:

MATCH (p:Person {name: "Alice"})  
RETURN p  
'''