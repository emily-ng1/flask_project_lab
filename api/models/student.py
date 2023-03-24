class Student:
    __table__="students"
    columns=["id", "last_name", "first_name", "ssn", "test1", "test2", "test3", "test4", "final", "grade"]

    def __init__(self, attrs):
        self.__dict__=dict(zip(self.columns, attrs))

    @classmethod
    def highest_final(self, cursor):
        cursor.execute(f"SELECT * FROM {self.__table__} ORDER BY final DESC LIMIT 1;")
        record=cursor.fetchone()
        record_dict=dict(zip(self.columns, record))
        return record_dict
    
    @classmethod
    def high_final(self, cursor, final=80):
        cursor.execute(f"SELECT * FROM {self.__table__} WHERE final>%s", (final,))
        records=cursor.fetchall()
        record_dicts=[dict(zip(self.columns, record)) for record in records]
        return record_dicts
