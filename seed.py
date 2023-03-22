import psycopg2

conn=psycopg2.connect(database="student_grade_development", user="postgres", password="postgres")
cursor=conn.cursor()

cursor.execute("SELECT * FROM students;")
print(cursor.fetchone())
#(1, 'Alfalfa', '   Aloysius', '   123-45-6789', Decimal('40.0'), Decimal('90.0'), 
# Decimal('100.0'), Decimal('83.0'), Decimal('49.0'), '   D-', 
# datetime.datetime(2023, 3, 22, 14, 0, 26, 836915))



