from orm import auto_cursor, auto_commit


class Games:
    __name = 'Games'
    __fields = (
        'id', 'name', 'city', 'begin', 'system',
        'tours_count', 'min_rating', 'time_on_game'
    )

    def __init__(self, connection):
        self.connection = connection

    @auto_commit
    def create(self, cursor):
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {self.__name} (
                id INTEGER PRIMARY KEY,
                name TEXT,
                city TEXT,
                begin REAL,
                system TEXT,
                tours_count INTEGER,
                min_rating INTEGER,
                time_on_game INTEGER
            )
        ''')

    @auto_commit
    def insert(self, cursor, entry):
        cursor.execute(f'''
            INSERT INTO {self.__name} (
                id, name, city, begin, system, tours_count,
                min_rating, time_on_game
            ) VALUES (
                ?, ?, ?, ?, ?, ?,
                ?, ?
            )
        ''', entry)

    @auto_cursor
    def get_top_sorted(self, cursor, field_name):
        cursor.execute(f"""
            SELECT * FROM {self.__name}
            ORDER BY {field_name}
            LIMIT 10
        """)
        return cursor.fetchall()

    @auto_cursor
    def count(self, cursor, sql_function, field_name):
        cursor.execute(f"""
            SELECT {sql_function}({field_name}) AS result
            FROM {self.__name}
        """)
        return cursor.fetchall()

    @auto_cursor
    def get_frequencies(self, cursor, field_name):
        cursor.execute(f"""
            SELECT {field_name}, COUNT(*) AS frequency
            FROM {self.__name}
            GROUP BY {field_name}
            ORDER BY frequency DESC;
        """)
        return cursor.fetchall()

    @auto_cursor
    def get_by_condition(self, cursor, field_name, condition, limit = 10):
        cursor.execute(f"""
            SELECT *
            FROM {self.__name}
            WHERE {condition}
            ORDER BY {field_name} DESC
            LIMIT {limit}
        """)
        return cursor.fetchall()

    def entries_to_dict(self, entries):
        result = []
        for entry in entries:
            d = {}
            for i in range(len(self.__fields)):
                d[self.__fields[i]] = entry[i]
            result.append(d)
        return result

    def __del__(self):
        self.connection.close()
        print('Connection to DB closed')
