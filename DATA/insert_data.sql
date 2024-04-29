-- Insert data into the Cities table
INSERT INTO Cities (name) VALUES 
('New York'), ('Los Angeles'), ('Chicago');

-- Insert data into the People table
INSERT INTO People (name, age, city_id) VALUES 
('John', 30, 1),
('Alice', 25, 2),
('Bob', 35, 3);

-- Insert data into the Houses table
INSERT INTO Houses (address, city_id) VALUES 
('123 Main St', 1),
('456 Elm St', 2),
('789 Oak St', 3);
