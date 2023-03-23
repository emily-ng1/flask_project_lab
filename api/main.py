from flask import Flask, jsonify
import psycopg2
from settings import db_name, user_name, password_name

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
    return jsonify(student_tuples)

@app.route("/students/<student_id>")
def student_show(student_id):
    conn=psycopg2.connect(database=app.config["DATABASE_NAME"], user=app.config["USER_NAME"], password=app.config["PASSWORD_NAME"])
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id=%s;", (student_id,))
    student_tuple=cursor.fetchone()
    return jsonify(student_tuple)


app.run(debug=True)
