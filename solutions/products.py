from orm import TableORM, auto_commit, auto_cursor


class Products(TableORM):
    def __init__(self, connection):
        super().__init__(connection, 'Products', {
            'id': 'INTEGER PRIMARY KEY',
            'name': 'TEXT',
            'price': 'REAL',
            'quantity': 'INTEGER',
            'category': 'TEXT',
            'fromCity': 'TEXT',
            'isAvailable': 'INTEGER',
            'views': 'INTEGER',
            'changes': 'INTEGER'
        })

    @auto_commit
    def create(self, cursor):
        field_pairs = list(zip(self.fields.keys(), self.fields.values()))
        field_pairs = tuple(map(lambda p: ' '.join(p), field_pairs))
        cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {self.name} (
                    {', '.join(field_pairs)}
                )
            """)

    @auto_commit
    def insert(self, cursor, entry):
        cursor.execute(f"""
                INSERT INTO {self.name} (
                    {', '.join(self.field_names)}
                ) VALUES (
                    {', '.join(['?'] * len(self.field_names))}
                )
            """, entry)

    @auto_commit
    def update(self, cursor, entry, condition):
        cursor.execute(f"""
                UPDATE {self.name}
                SET {entry[0]} = {entry[1]}, changes = changes + 1
                WHERE {condition};
            """)

    @auto_commit
    def delete(self, cursor, condition):
        cursor.execute(f"""
                        DELETE FROM {self.name}
                        WHERE {condition};
                    """)