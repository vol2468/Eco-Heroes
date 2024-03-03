DROP TABLE IF EXISTS kids;
DROP TABLE IF EXISTS sdgs;
DROP TABLE IF EXISTS city;

CREATE TABLE kids (
    username varchar(20) PRIMARY KEY,
    city varchar(20),
    latitude DECIMAL(17,3),
    longitude DECIMAL(17,3)
);
CREATE TABLE sdgs (
    id INTEGER PRIMARY KEY,
    img BLOB,
    description varchar(100)
);

CREATE TABLE city (
    cname varchar(20),
    latitude DECIMAL(17,3),
    longitude DECIMAL(17,3)
);

