CREATE DATABASE IF NOT EXISTS sqi_lms_db
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE sqi_lms_db;

CREATE TABLE users (
    id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(20),              -- student / instructor / admin
    created_at DATETIME
);

CREATE TABLE courses (
    id INT PRIMARY KEY,
    instructor_id INT NOT NULL, 
    title VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    duration VARCHAR(50),
    created_at DATETIME,
    INDEX idx_courses_instructor_id (instructor_id),
    CONSTRAINT fk_courses_instructor FOREIGN KEY (instructor_id) REFERENCES users(id)
);

CREATE TABLE enrollments (
    id INT PRIMARY KEY,
    user_id INT NOT NULL,
    course_id INT NOT NULL,
    enrolled_at DATETIME,
    status VARCHAR(20),            -- active / completed / dropped
    INDEX idx_enrollments_user_id (user_id),
    INDEX idx_enrollments_course_id (course_id),
    CONSTRAINT fk_enrollments_user FOREIGN KEY (user_id) REFERENCES users(id),
    CONSTRAINT fk_enrollments_course FOREIGN KEY (course_id) REFERENCES courses(id)
);

CREATE TABLE lessons (
    id INT PRIMARY KEY,
    course_id INT NOT NULL,
    title VARCHAR(100) NOT NULL,
    content TEXT,
    video_url VARCHAR(255),
    lesson_order INT,
    created_at DATETIME,
    INDEX idx_lessons_course_id (course_id),
    CONSTRAINT fk_lessons_course FOREIGN KEY (course_id) REFERENCES courses(id)
);

CREATE TABLE assignments (
    id INT PRIMARY KEY,
    course_id INT NOT NULL,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    due_date DATE,
    created_at DATETIME,
    INDEX idx_assignments_course_id (course_id),
    CONSTRAINT fk_assignments_course FOREIGN KEY (course_id) REFERENCES courses(id)
);

CREATE TABLE submissions (
    id INT PRIMARY KEY,
    assignment_id INT NOT NULL,
    user_id INT NOT NULL,
    submission_file VARCHAR(255),
    score DECIMAL(5,2) NULL,       -- NULL until graded
    submitted_at DATETIME,
    INDEX idx_submissions_assignment_id (assignment_id),
    INDEX idx_submissions_user_id (user_id),
    CONSTRAINT fk_submissions_assignment FOREIGN KEY (assignment_id) REFERENCES assignments(id),
    CONSTRAINT fk_submissions_user FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE quizzes (
    id INT PRIMARY KEY,
    course_id INT NOT NULL,
    title VARCHAR(100) NOT NULL,
    total_marks INT,
    duration INT,                  -- minutes
    created_at DATETIME,
    INDEX idx_quizzes_course_id (course_id),
    CONSTRAINT fk_quizzes_course FOREIGN KEY (course_id) REFERENCES courses(id)
);

CREATE TABLE quiz_results (
    id INT PRIMARY KEY,
    quiz_id INT NOT NULL,
    user_id INT NOT NULL,
    score DECIMAL(5,2),
    attempted_at DATETIME,
    INDEX idx_quiz_results_quiz_id (quiz_id),
    INDEX idx_quiz_results_user_id (user_id),
    CONSTRAINT fk_quiz_results_quiz FOREIGN KEY (quiz_id) REFERENCES quizzes(id),
    CONSTRAINT fk_quiz_results_user FOREIGN KEY (user_id) REFERENCES users(id)
);
