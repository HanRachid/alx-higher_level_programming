-- create multiple rows in a new TABLE
CREATE TABLE IF NOT EXISTS second_table(
	id int NOT NULL,
	name varchar(256) NOT NULL,
	score INT NOT NULL
	);

INSERT INTO second_table (id,name,score)
VALUES (1,'John',10),
(2,'Alex',3),
(3,'Bob',14),
(4,'George',8);