CREATE DATABASE IF NOT EXISTS employee;
USE employee;

CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    position VARCHAR(255),
    salary DECIMAL(10, 2)
);

INSERT INTO employees (name, position, salary)
VALUES ('John Doe', 'Software Engineer', 75000),
       ('Jane Smith', 'Project Manager', 85000),
       ('Emily Johnson', 'Designer', 70000);
