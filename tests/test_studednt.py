from api.models.student import Student

def test_init_student():
    student=Student(["1", "Alfalfa", "Aloysius", "123-45-6789", "40.0", "90.0", "100.0", "83.0", "49.0", "D-"])
    assert student.grade=="D-"