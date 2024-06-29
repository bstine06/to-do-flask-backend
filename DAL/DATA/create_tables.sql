

CREATE TABLE Projects (
    id INTEGER PRIMARY KEY,
    uuid VARCHAR(36) NOT NULL UNIQUE,
    name TEXT NOT NULL
);

CREATE TABLE Tasks (
    id INTEGER PRIMARY KEY,
    uuid VARCHAR(36) NOT NULL UNIQUE,
    name TEXT NOT NULL,
    description TEXT,
    due_date DATE NOT NULL,
    priority TEXT NOT NULL,
    notes TEXT,
    project_id INTEGER,
    FOREIGN KEY (project_id) REFERENCES Projects(id)
);

CREATE INDEX idx_tasks_project_id ON Tasks(project_id);