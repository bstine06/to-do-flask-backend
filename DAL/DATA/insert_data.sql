-- Insert sample data into Projects table
INSERT INTO Projects (id, name) VALUES
(1, 'Project Alpha'),
(2, 'Project Beta'),
(3, 'Project Gamma');

-- Insert sample data into Tasks table with UUIDs
INSERT INTO Tasks (id, uuid, name, description, due_date, priority, notes, project_id) VALUES
(1, 'ff8e4c7f-d8b5-477c-9829-a5133c4b5ace', 'Task 1', 'Description for Task 1', '2024-07-01', 1, 'Notes for Task 1', 1),
(2, '0752d42e-e108-4f03-b958-ce367561590a', 'Task 2', 'Description for Task 2', '2024-07-02', 2, 'Notes for Task 2', 1),
(3, '9993da26-2a32-4dad-a17a-ccd8282e1e78', 'Task 3', 'Description for Task 3', '2024-07-03', 3, 'Notes for Task 3', 2),
(4, '01ce15dd-227c-4f29-8781-cce6ed687f99', 'Task 4', 'Description for Task 4', '2024-07-04', 2, 'Notes for Task 4', 2),
(5, 'a8337833-57d2-470b-97aa-ed332c2f2712', 'Task 5', 'Description for Task 5', '2024-07-05', 1, 'Notes for Task 5', 3);