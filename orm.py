from abc import abstractmethod


def auto_cursor(func):
    def act(self, *args):
        cursor = self.connection.cursor()
        return func(self, cursor, *args)

    return act


def auto_commit(func):
    def act(self, *args):
        cursor = self.connection.cursor()
        func(self, cursor, *args)
        self.connection.commit()

    return act


class TableORM:
    def __init__(self, connection, name, fields: dict[str, str]):
        self.connection = connection
        self.name = name
        self.fields = fields
        self.field_names = tuple(fields.keys())

    def __del__(self):
        self.connection.close()
        print('Connection to DB closed')

    @abstractmethod
    def create(self, cursor):
        pass

    @abstractmethod
    def insert(self, cursor, entry):
        pass

    @auto_cursor
    def get_top_sorted(self, cursor, field_name, limit):
        cursor.execute(f"""
                SELECT * FROM {self.name}
                ORDER BY {field_name}
                LIMIT {limit}
            """)
        return cursor.fetchall()

    @auto_cursor
    def count(self, cursor, sql_function, field_name):
        cursor.execute(f"""
                SELECT {sql_function}({field_name}) AS result
                FROM {self.name}
            """)
        return cursor.fetchall()

    @auto_cursor
    def get_frequencies(self, cursor, field_name):
        cursor.execute(f"""
                SELECT {field_name}, COUNT(*) AS frequency
                FROM {self.name}
                GROUP BY {field_name}
                ORDER BY frequency DESC;
            """)
        return cursor.fetchall()

    @auto_cursor
    def get_by_condition(self, cursor, field_name, condition, limit=10):
        cursor.execute(f"""
                SELECT *
                FROM {self.name}
                WHERE {condition}
                ORDER BY {field_name} DESC
                LIMIT {limit}
            """)
        return cursor.fetchall()

    def entries_to_dict(self, entries):
        result = []
        for entry in entries:
            d = {}
            for i in range(len(self.field_names)):
                d[self.field_names[i]] = entry[i]
            result.append(d)
        return result
