import psycopg2
from api.models.student import Student


conn=psycopg2.connect(database="student_grade_development", user="postgres", password="postgres")
cursor=conn.cursor()

cursor.execute("SELECT * FROM students;")
print(cursor.fetchone())
#(1, 'Alfalfa', 'Aloysius', '123-45-6789', 
# Decimal('40.0'), Decimal('90.0'), Decimal('100.0'), Decimal('83.0'), Decimal('49.0'), 
# 'D-', datetime.datetime(2023, 3, 22, 17, 49, 16, 324915))


student=Student(["1", "Alfalfa", "Aloysius", "123-45-6789", "40.0", "90.0", "100.0", "83.0", "49.0", "D-"])
#student #<api.models.student.Student object at 0x10388c1d0>
#student.__dict__ #{'id': '1', 'last_name': 'Alfalfa', 'first_name': 'Aloysius', 'ssn': '123-45-6789', 'test1': '40.0', 'test2': '90.0', 'test3': '100.0', 'test4': '83.0', 'final': '49.0', 'grade': 'D-'}