# Neo4j

## Local setup using docker

```sh
docker rm neo4j
docker pull neo4j:4.4
docker run --name neo4j -p 7474:7474 -p 7687:7687 -e NEO4J_AUTH=neo4j/secret neo4j:4.4
```
