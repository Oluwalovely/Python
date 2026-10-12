import mysql.connector as sql
# print("import successful")

conn = sql.connect(
    host = "127.0.0.1",
    port = "3306",
    user = "root",
    password = "",
    database = "sqi_lms_db"
)

conn.autocommit = True
mycursor = conn.cursor()
print("database connected successfully")

# query = "SHOW DATABASES"
# query = """CREATE TABLE questions(
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     quizz_id INT NOT NULL,
#     question VARCHAR(500) NOT NULL,
#     option_a VARCHAR(500) NOT NULL,
#     option_b VARCHAR(500) NOT NULL,
#     option_c VARCHAR(500) NOT NULL,
#     option_d VARCHAR(500) NOT NULL,

#     correct_option ENUM('A', 'B', 'C', 'D') NOT NULL,

#     CONSTRAINT fk_questions_quiz FOREIGN KEY (quizz_id)
#     REFERENCES quizzes(id) ON DELETE CASCADE

# )"""

# query = "ALTER TABLE users ADD phone_number VARCHAR(14)"
query = "ALTER TABLE users RENAME COLUMN phone_number TO phoneNumber"
# query = "ALTER TABLE users RENAME COLUMN Password TO password_hashed"
# query = "ALTER TABLE users DROP PhoneNumber"
# query = "INSERT INTO users(first_name, last_name, email, password, role) VALUES(%s,%s,%s,%s,%s)"
# values = ("emmie", "bayor", "embayor@gmail.com", "12345", "admin")
# query = "UPDATE users SET first_name=%s WHERE id=%s"
# values = ("Lovely", 4)
# query = "DELETE FROM users WHERE id=%s"
# values = (4,)

# query = "SELECT * FROM users WHERE id = %s"
# mycursor.execute(query, (10,))
# users = mycursor.fetchone()
# print(users)
mycursor.execute(query)
print("query successfully made")