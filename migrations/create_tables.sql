DROP TABLE IF EXISTS students;

CREATE TABLE IF NOT EXISTS students(
    id serial PRIMARY KEY,
    last_name VARCHAR(255) NOT NULL, 
    first_name VARCHAR(255) NOT NULL,
    ssn VARCHAR(255),
    test1 DECIMAL,
    test2 DECIMAL,
    test3 DECIMAL,
    test4 DECIMAL,
    final DECIMAL,
    grade VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS students_grade_index ON students (grade);