-- SELECT * FROM users WHERE last_name = "Eboh";
-- SELECT first_name, last_name FROM users;
-- SELECT * FROM submissions WHERE score >= 50;
-- SELECT score FROM submissions WHERE user_id = 19;
-- SELECT * FROM submissions ORDER BY score DESC;
-- SELECT * FROM submissions ORDER BY score ASC;
-- SELECT * FROM submissions ORDER BY score DESC LIMIT 5;
-- SELECT COUNT(*) FROM users;
-- SELECT AVG(score) AS avg_score FROM submissions;
-- SELECT * FROM submissions;
-- SELECT courses.title, courses.description, courses.duration, user.first_name FROM courses JOIN users ON instructor_id


-- aggregations

-- OR, AND, SUM, AVG, BETWEEN, NOT
-- SELECT * FROM submissions WHERE score > 50 AND id < 20
-- SELECT * FROM users WHERE role = "student" OR role = "instructor"
-- SELECT * FROM users WHERE NOT role ="admin"
-- SELECT * FROM submissions WHERE score BETWEEN 50 AND 100;
-- SELECT * FROM users WHERE first_name LIKE "E%"; #starts with E 
-- SELECT * FROM users WHERE first_name LIKE "%E"; # ends with E
-- SELECT * FROM users WHERE first_name LIKE "%E%"; # contains E

-- SELECT * FROM submissions ORDER BY score
-- SELECT * FROM submissions ORDER BY score DESC 
-- SELECT * FROM submissions ORDER BY score DESC LIMIT 5
-- SELECT AVG(score) FROM submissions
-- SELECT MIN(score) FROM submissions
-- SELECT MAX(score) FROM submissions
-- SELECT AVG(score) FROM submissions
-- SELECT role, COUNT(*) FROM users GROUP BY role
-- SELECT course_id, COUNT(*) FROM enrollments GROUP BY course_id

-- SELECT assignments.title, AVG(submissions.score) AS average_score
-- FROM assignments
-- JOIN submissions ON assignments.id
-- GROUP BY assignments.title, assignments.id


-- find courses with more than five students, display course title, number of students, only show courses with more than 5 students. Sort from higest to lowestest
-- SELECT courses.title, COUNT(enrollments.user_id) AS number_of_students 
-- FROM courses 
-- JOIN enrollments ON courses.id = enrollments.course_id
-- JOIN users ON users.id = enrollments.user_id WHERE users.role = 'student'
-- GROUP BY courses.title, courses.id HAVING COUNT(enrollments.user_id) > 5
-- ORDER BY number_of_students DESC 


-- show every students enrolled in courses, display student firstname, lastname, course title, enrollment status and only student should appear.

10. Show each course and its instructor

Display:

course title
instructor first name
instructor last name

Remember that both students and instructors are stored inside the same users table.

Concepts: JOIN, table aliases

QUERY:
SELECT courses.title, users.first_name AS instructor_first_name, users.last_name AS instructor_last_name, users.role 
FROM courses 
JOIN users ON users.id = courses.instructor_id;


11. Find the highest and lowest score

Display:

highest score
lowest score
average score

from the submissions table.

Concepts: MAX(), MIN(), AVG()

QUERY:
SELECT MIN(score), min(score), avg(score) FROM submissions

12. Find students who have not submitted an assignment

Display students who are enrolled in at least one course but do not have a submission record for an assignment.

Display:

student name
course

Concepts: JOIN, LEFT JOIN, IS NULL

QUERY:
SELECT  users.first_name, 
		users.last_name, 
        courses.title AS course, 
        assignments.title AS assignments,
        submissions.submitted_at
FROM enrollments
JOIN users ON users.id = enrollments.user_id
JOIN courses on courses.id = enrollments.course_id
JOIN assignments on courses.id = assignments.course_id
LEFT JOIN submissions
        ON submissions.assignment_id = assignments.id
        AND submissions.user_id = users.id
        AND users.role = 'student'
WHERE submissions.id IS NULL;

13. Find courses with no enrolled students

Display all courses that currently have zero students enrolled.

Display:

course_id
course title

Concepts: LEFT JOIN, IS NULL

QUERY:
SELECT courses.id AS course_id, courses.title
FROM courses
LEFT JOIN enrollments
        ON enrollments.course_id = courses.id
WHERE enrollments.id IS NULL;

CROSSCHECK:
SELECT courses.id, courses.title, COUNT(enrollments.id) AS enrolled
FROM courses
LEFT JOIN enrollments ON enrollments.course_id = courses.id
GROUP BY courses.id, courses.title;

14. Grade every submission

Create a result containing:

user_id
score
grade

Use the following grading system:

70 and above → A
60–69        → B
50–59        → C
40–49        → D
Below 40     → F

Use a SQL CASE expression.

Concepts: CASE, comparison operators, aliases

QUERY:
SELECT submissions.user_id, submissions.score,
       CASE
           WHEN submissions.score IS NULL THEN 'Not graded'
           WHEN submissions.score >= 70 THEN 'A'
           WHEN submissions.score >= 60 THEN 'B'
           WHEN submissions.score >= 50 THEN 'C'
           WHEN submissions.score >= 40 THEN 'D'
           ELSE 'F'
       END AS grade
FROM submissions;

15. Find students above the average score

Display:

student first name
student last name
score

Only show students whose score is greater than the overall average submission score.

Concepts: JOIN, AVG(), subquery, WHERE