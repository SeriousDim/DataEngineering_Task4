from orm import auto_commit


class Prizes:
    __name = 'Prizes'
    __fields = (
        'name', 'place', 'prize'
    )

    def __init__(self, connection):
        self.connection = connection

    @auto_commit
    def create(self, cursor):
        cursor.execute(f'''
                CREATE TABLE IF NOT EXISTS {self.__name} (
                    name TEXT,
                    place INTEGER,
                    prize INTEGER
                )
            ''')

    @auto_commit
    def insert(self, cursor, entry):
        cursor.execute(f'''
                INSERT INTO {self.__name} {self.__fields} VALUES (
                    ?, ?, ?
                )
            ''', entry)
