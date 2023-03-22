from flask import Flask, jsonify
import psycopg2

app=Flask(__name__)

@app.route("/")
def home_page():
    return "Welcome to the Student's Grade Page!"

@app.route("/students")
def student_index():
    conn=psycopg2.connect(database="student_grade_development", user="postgres", password="postgres")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM students;")
    student_tuples=cursor.fetchall()
    return jsonify(student_tuples)

@app.route("/students/<student_id>")
def student_show(student_id):
    conn=psycopg2.connect(database="student_grade_development", user="postgres", password="postgres")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id=%s;", (student_id,))
    student_tuple=cursor.fetchone()
    return jsonify(student_tuple)


app.run(debug=True)
