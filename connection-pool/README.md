# Setup

## Run mysql using docker locally

- Pull the latest image:
    `docker pull mysql:latest`

- Run the docker image:
    `docker run --name trial-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -p 3306:3306 -d mysql:latest --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci --bind-address=0.0.0.0`

- Ensure it is running
    `docker ps`

## Stop the container
`docker stop trial-mysql`
`docker rm trial-mysql`
