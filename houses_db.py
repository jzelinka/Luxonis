from typing import Any
import psycopg2


class db_handler:
    def __init__(self) -> None:
        dbname = "postgres"
        user = "postgres"
        password = "postgres"
        host = "localhost"
        port = "5432"  # Default PostgreSQL port

        self.create_query = "CREATE TABLE houses (name varchar(100), location varchar(100), image_url varchar(1000));"
        self.select_query = "select * from houses;"
        self.insert_query = "insert into houses values (%s, %s, %s);"
        self.delete_query = "DROP TABLE IF EXISTS houses;"

        self.connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cursor = self.connection.cursor()
    
    def delete_table(self):
        self.cursor.execute(self.delete_query)
        self.connection.commit()
    
    def create_table(self):
        self.cursor.execute(self.create_query)
        self.connection.commit()
    
    def insert(self, name, location, image_url):
        self.cursor.execute(self.insert_query, (name, location, image_url))
        self.connection.commit()
    
    def get_rows(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM houses;")
        rows = cursor.fetchall()
        cursor.close()
        return rows
    
    def __del__(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()

if __name__ == "__main__":
    db = db_handler()
    db.delete_table()
    db.create_table()
    db.insert("test", "test", "test")
    db.insert("test2", "test", "test")
    print(db.get_rows())