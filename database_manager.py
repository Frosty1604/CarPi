import sqlite3


class DatabaseManager:

    def __init__(self, db_name: str):
        self.conn = sqlite3.connect(db_name + ".db")
        self.tables = []

    def create_table(self, table_name: str):
        try:
            self.conn.execute("CREATE TABLE " + table_name + "(" + table_name + " CHAR)")
            self.tables.append(table_name)
        except Exception as e:
            print(e)

    def get_tables(self):
        index = 0
        for table in self.tables:
            print("#" + str(index) + " " + table)
            index += 1

    def add_data(self, table_name: str, data):
        self.conn.execute("INSERT INTO " + table_name + " VALUES(?)", data)
        self.conn.commit()

    def get_all_data(self, table_name: str):
        cur = self.conn.cursor()
        data = []

        cur.execute("SELECT " + table_name + " FROM " + table_name)

        rows = cur.fetchall()

        for row in rows:
            data.append(row[0])

        return data
