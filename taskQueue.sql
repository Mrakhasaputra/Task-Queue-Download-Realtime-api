CREATE TABLE task_queue (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    status VARCHAR(50),
    file_path VARCHAR(255),
    created_at VARCHAR(50)
);
