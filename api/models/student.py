class Student:
    columns=["id", "last_name", "first_name", "ssn", "test1", "test2", "test3", "test4", "final", "grade"]

    def __init__(self, attrs):
        self.__dict__=dict(zip(self.columns, attrs))
