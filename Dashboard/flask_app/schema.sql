DROP TABLE IF EXISTS kids;
DROP TABLE IF EXISTS sdgs;

CREATE TABLE kids (
    username varchar(20) PRIMARY KEY,
    city varchar(20),
    latitude NUMERIC,
    longitude INT
);
CREATE TABLE sdgs (
    id INTEGER PRIMARY KEY,
    img IMAGE,
    explanation varchar(100)
);

CREATE TABLE city (
    id INTEGER PRIMARY KEY,
    img IMAGE,
    explanation varchar(100)
);

