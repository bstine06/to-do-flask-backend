CREATE TABLE People (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    city_id INTEGER,
    FOREIGN KEY (city_id) REFERENCES Cities(id)
);

CREATE TABLE Houses (
    id INTEGER PRIMARY KEY,
    address TEXT,
    city_id INTEGER,
    FOREIGN KEY (city_id) REFERENCES Cities(id)
);

CREATE TABLE Cities (
    id INTEGER PRIMARY KEY,
    name TEXT
);
