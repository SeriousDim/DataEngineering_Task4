from orm import TableORM, auto_commit


class Songs(TableORM):

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
            SET explicit = {entry[0]}, loudness = {entry[1]}
            WHERE {condition};
        """)
