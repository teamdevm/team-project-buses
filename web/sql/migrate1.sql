CREATE TABLE db_ver(
	db_ver INTEGER
);

INSERT INTO db_ver(db_ver) values(0);

CREATE TABLE user (
	id INTEGER PRIMARY KEY,
	login varchar(32),
	password  TEXT,
	registration_date INTEGER
);


