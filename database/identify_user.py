"""This module contains code to identify users between sessions."""
import mysql.connector

from config import Config


class Database:
    def __init__(self):
        self.user = Config.DB_USER
        self.password = Config.DB_PASSWORD
        self.host = Config.DB_HOST
        self.database = Config.DB_NAME
        self.connection = None

    def __enter__(self):
        """Open a MySQL connection when entering context."""
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
        )
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close a MySQL connection when exiting context."""
        if self.connection:
            self.connection.close()


class DatabaseUser(Database):
    def __init__(self, user: str, password: str, host: str, database: str, user_id: str):
        super().__init__(user, password, host, database)
        self.uuid = user_id

    def get_or_create_user(self, token: str):
        with Database() as connection:
            cursor = connection.cursor()

            cursor.execute("""CREATE TABLE IF NOT EXISTS user (
                           id INT PRIMARY KEY AUTO_INCREMENT,
                           token VARCHAR(100) NOT NULL UNIQUE,
                           uuid VARCHAR(100) NOT NULL UNIQUE,
                           timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)""")

            cursor.execute("""SELECT uuid FROM polling.user WHERE uuid = ?""", self.uuid)
            result = cursor.fetchone()

            if not result:
                cursor.execute("""INSERT INTO polling.user (token, uuid) VALUES (%s, %s)""", (token, self.uuid))
                connection.commit()
