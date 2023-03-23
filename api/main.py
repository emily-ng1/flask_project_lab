from flask import Flask, jsonify
import psycopg2
from settings import db_name, user_name, password_name
from models.student import Student

app=Flask(__name__)

app.config.from_mapping(
    DATABASE_NAME=db_name,
    USER_NAME=user_name,
    PASSWORD_NAME=password_name
)

@app.route("/")
def home_page():
    return "Welcome to the Student's Grade Page!"

@app.route("/students")
def student_index():
    conn=psycopg2.connect(database=app.config["DATABASE_NAME"], user=app.config["USER_NAME"], password=app.config["PASSWORD_NAME"])
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM students;")
    student_tuples=cursor.fetchall()
    student_dicts=[Student(student_tuple).__dict__ for student_tuple in student_tuples]
    return jsonify(student_dicts)

@app.route("/students/<student_id>")
def student_show(student_id):
    conn=psycopg2.connect(database=app.config["DATABASE_NAME"], user=app.config["USER_NAME"], password=app.config["PASSWORD_NAME"])
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id=%s;", (student_id,))
    student_tuple=cursor.fetchone()
    student_dict=Student(student_tuple).__dict__
    return jsonify(student_dict)


app.run(debug=True)

