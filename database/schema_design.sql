CREATE DATABASE student_management;
USE student_management;
CREATE TABLE students(
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    register_number VARCHAR(20) UNIQUE,
    full_name VARCHAR(30),
    e_mail VARCHAR(50),
    date_of_birth DATE,
    gender VARCHAR(1),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE subjects(
    subject_id INT PRIMARY KEY AUTO_INCREMENT,
    subject_code VARCHAR(15),
    subject_name VARCHAR(50),
    credits INT
);

CREATE TABLE marks(
    marks_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    subject_id INT,
    marks INT,
    grade VARCHAR(3),
    FOREIGN KEY(student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY(subject_id) REFERENCES subjects(subject_id) ON DELETE CASCADE
);
