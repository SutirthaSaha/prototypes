CREATE DATABASE IF NOT EXISTS zomato;
USE zomato;

CREATE TABLE IF NOT EXISTS agent (
    id INT AUTOINCREMENT PRIMARY KEY,
    is_reserved TINYINT(1) NOT NULL DEFAULT 0,
    order_id INT
);

CREATE TABLE IF NOT EXISTS food (
    id INT AUTOINCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS packet (
    id INT AUTOINCREMENT PRIMARY KEY,
    food_id INT,
    is_reserved TINYINT(1) NOT NULL DEFAULT 0,
    order_id INT,
    FOREIGN KEY (food_id) REFERENCES food(id)
);

INSERT INTO food (name) VALUES ('Pizza');
INSERT INTO food (name) VALUES ('Burger');
INSERT INTO food (name) VALUES ('Sushi');
INSERT INTO food (name) VALUES ('Pasta');

INSERT INTO agent (is_reserved) VALUES (0);
INSERT INTO agent (is_reserved) VALUES (0);
INSERT INTO agent (is_reserved) VALUES (0);
INSERT INTO agent (is_reserved) VALUES (0);
INSERT INTO agent (is_reserved) VALUES (0);
INSERT INTO agent (is_reserved) VALUES (0);

-- Packets for Pizza
INSERT INTO packet (food_id, is_reserved, order_id) VALUES (1, 0, NULL);
INSERT INTO packet (food_id, is_reserved, order_id) VALUES (1, 0, NULL);
INSERT INTO packet (food_id, is_reserved, order_id) VALUES (1, 0, NULL);

-- Packets for Burger
INSERT INTO packet (food_id, is_reserved, order_id) VALUES (2, 0, NULL);
INSERT INTO packet (food_id, is_reserved, order_id) VALUES (2, 0, NULL);
INSERT INTO packet (food_id, is_reserved, order_id) VALUES (2, 0, NULL);

-- Packets for Sushi
INSERT INTO packet (food_id, is_reserved, order_id) VALUES (3, 0, NULL);
INSERT INTO packet (food_id, is_reserved, order_id) VALUES (3, 0, NULL);
INSERT INTO packet (food_id, is_reserved, order_id) VALUES (3, 0, NULL);

-- Packets for Pasta
INSERT INTO packet (food_id, is_reserved, order_id) VALUES (4, 0, NULL);
INSERT INTO packet (food_id, is_reserved, order_id) VALUES (4, 0, NULL);
INSERT INTO packet (food_id, is_reserved, order_id) VALUES (4, 0, NULL);
