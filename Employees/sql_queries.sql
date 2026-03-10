-- Create database
CREATE DATABASE sql_practice;
\c sql_practice

-- Create tables
CREATE TABLE departments (
    dept_id SERIAL PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL,
    location VARCHAR(100),
    budget DECIMAL(12, 2)
);

CREATE TABLE employees (
    emp_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    hire_date DATE DEFAULT CURRENT_DATE,
    salary DECIMAL(10, 2),
    dept_id INTEGER REFERENCES departments(dept_id)
);

CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY,
    project_name VARCHAR(100) NOT NULL,
    start_date DATE,
    end_date DATE,
    budget DECIMAL(12, 2),
    dept_id INTEGER REFERENCES departments(dept_id)
);

-- Insert sample data
INSERT INTO departments (dept_name, location, budget) VALUES
('Engineering', 'Building A', 500000),
('Sales', 'Building B', 300000),
('Marketing', 'Building C', 200000),
('HR', 'Building D', 150000);

INSERT INTO employees (first_name, last_name, email, hire_date, salary, dept_id) VALUES
('Alice', 'Johnson', 'alice@company.com', '2020-03-15', 85000, 1),
('Bob', 'Smith', 'bob@company.com', '2019-07-01', 72000, 1),
('Carol', 'Williams', 'carol@company.com', '2021-01-10', 65000, 2),
('David', 'Brown', 'david@company.com', '2018-11-20', 90000, 1),
('Eve', 'Davis', 'eve@company.com', '2022-05-01', 55000, 3),
('Frank', 'Miller', 'frank@company.com', '2020-09-15', 78000, 2),
('Grace', 'Wilson', 'grace@company.com', '2021-06-01', 62000, 4),
('Henry', 'Taylor', 'henry@company.com', '2019-03-01', 95000, 1);

INSERT INTO projects (project_name, start_date, end_date, budget, dept_id) VALUES
('Website Redesign', '2024-01-01', '2024-06-30', 50000, 3),
('Mobile App', '2024-02-15', '2024-12-31', 150000, 1),
('Sales Portal', '2024-03-01', '2024-09-30', 75000, 2),
('HR System', '2024-04-01', '2024-08-31', 40000, 4);

-- DDL Practice

ALTER TABLE employees ADD COLUMN phone VARCHAR(20);

ALTER TABLE departments ALTER COLUMN budget SET DATA TYPE DECIMAL(15, 2);

CREATE TABLE training_courses (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    duration_hours INTEGER,
    instructor VARCHAR(100) UNIQUE NOT NULL
)

/* DROP TABLE training_courses; */

-- DML Practice 

INSERT INTO employees (first_name, last_name, email, salary, dept_id) VALUES
('Grace', 'Lee', 'grace.lee@company.com', 58000, 4),
('Ivan', 'Chen', 'ivan@company.com', 61000, 4),
('Julia', 'Kim', 'julia@company.com', 55000, 4);

UPDATE employees SET salary = salary * 1.05 WHERE dept_id = 1;
UPDATE employees SET email = 'bob.smith@company.com' WHERE emp_id = 2;

-- This does run, but I don't want to run it
DELETE FROM projects WHERE end_date < CURRENT_DATE;
DELETE FROM employees WHERE dept_id = NULL;
-- Could be bad as this has potential to completely remove all employees if the condition is not correct

-- DQL Practice
SELECT * FROM employees ORDER BY salary DESC;
SELECT * FROM employees WHERE dept_id = 1;
SELECT * FROM employees WHERE hire_date > '2021-01-01';

SELECT * FROM employees WHERE salary > 60000 AND salary < 80000;
SELECT * FROM employees WHERE email LIKE '%company%';
SELECT * FROM employees WHERE dept_id IN (1, 2);

SELECT dept_id, SUM(salary) FROM employees GROUP BY dept_id;
SELECT AVG(salary) FROM employees;
SELECT MAX(salary) FROM employees;
SELECT MIN(salary) FROM employees;
SELECT dept_id, COUNT(*) FROM employees GROUP BY dept_id HAVING COUNT(*) >= 2;

SELECT (e.first_name || ' ' || e.last_name) AS full_name, d.dept_name, e.salary FROM employees e JOIN departments d ON e.dept_id = d.dept_id;

-- Challenge

-- List employees where salary is greater than the average salary
SELECT * FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);

-- List departments with at least one project
SELECT * FROM departments d WHERE EXISTS (SELECT 1 FROM projects p WHERE p.dept_id = d.dept_id);

-- List employees with the highest salary in each department
SELECT * FROM employees e WHERE salary = (SELECT MAX(salary) FROM employees WHERE dept_id = e.dept_id);