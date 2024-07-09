-- Drop existing tables if they exist
DROP TABLE IF EXISTS Tasks;
DROP TABLE IF EXISTS Projects;

-- Create Projects table with UUID as primary key
CREATE TABLE Projects (
    uuid VARCHAR(36) PRIMARY KEY,
    name TEXT NOT NULL
);

-- Create Tasks table with project UUID as foreign key
CREATE TABLE Tasks (
    id INTEGER PRIMARY KEY,
    uuid VARCHAR(36) NOT NULL UNIQUE,
    name TEXT NOT NULL,
    description TEXT,
    due_date DATE NOT NULL,
    priority TEXT NOT NULL,
    notes TEXT,
    project_uuid VARCHAR(36),
    FOREIGN KEY (project_uuid) REFERENCES Projects(uuid)
);

-- Create index on project_uuid in Tasks table
CREATE INDEX idx_tasks_project_uuid ON Tasks(project_uuid);
