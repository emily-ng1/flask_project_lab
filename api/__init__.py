from flask import Flask, jsonify
import psycopg2
#from settings import db_name, user_name, password_name
from api.models.student import Student



def create_app(db_name, user_name, password_name):
    app=Flask(__name__)

    app.config.from_mapping(
        DATABASE_NAME=db_name,
        USER_NAME=user_name,
        PASSWORD_NAME=password_name
    )

    @app.route("/")
    def home_page():
        return "Welcome to the Student's Grade Page!"
    
    @app.route("/highest_final")
    def student_highest_final():
        conn=psycopg2.connect(database=app.config["DATABASE_NAME"], user=app.config["USER_NAME"], password=app.config["PASSWORD_NAME"])
        cursor=conn.cursor()
        high_final=Student.highest_final(cursor)
        return jsonify(high_final)

    @app.route("/high_final")
    def student_high_final():
        conn=psycopg2.connect(database=app.config["DATABASE_NAME"], user=app.config["USER_NAME"], password=app.config["PASSWORD_NAME"])
        cursor=conn.cursor()
        high_finals=Student.high_final(cursor)
        return jsonify(high_finals)

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
    
    return app


#app.run(debug=True)

