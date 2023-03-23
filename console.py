import psycopg2
from api.models.student import Student


conn=psycopg2.connect(database="student_grade_development", user="postgres", password="postgres")
cursor=conn.cursor()

cursor.execute("SELECT * FROM students;")
print(cursor.fetchone())
#(1, 'Alfalfa', 'Aloysius', '123-45-6789', 
# Decimal('40.0'), Decimal('90.0'), Decimal('100.0'), Decimal('83.0'), Decimal('49.0'), 
# 'D-', datetime.datetime(2023, 3, 22, 17, 49, 16, 324915))


student=Student(["Alfalfa", "Aloysius", "123-45-6789", "40.0", "90.0", "100.0", "83.0", "49.0", "D-"])
#student #<api.models.student.Student object at 0x101147fd0>
#student.__dict__ #{'id': 'Alfalfa', 'last_name': 'Aloysius', 'first_name': '123-45-6789', 'ssn': '40.0', 'test1': '90.0', 'test2': '100.0', 'test3': '83.0', 'test4': '49.0', 'final': 'D-'}
