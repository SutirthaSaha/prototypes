# Deadlock creation

This prototype is try and replicate a deadlock in mysql and how to react when such a scenario happens.
To try this out we need to first deploy mysql and also provide some initial data.

## Setup MySQL

- `initialize.sql`: a script to create the database, table and populate with dummy data
- `docker-compose.yml`: easy way to set up your mysql locally

Command:
```sh
cd mysql
docker-compose up
```