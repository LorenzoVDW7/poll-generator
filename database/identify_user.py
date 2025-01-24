"""This module contains code to identify users between sessions."""

import mysql.connector
import os
import uuid

from config import Config

class Database:
    def __init__(self, user: str, password: str, host: str, database: str):
        self.user = user
        self.password = password
        self.host = host
        self.database = database

    def open_connection(self):
        """Open a MySQL connection."""
        mydb = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
        )
        return mydb

class DatabaseUser(Database):
    def __init__(self, user: str, password: str, host: str, database: str, uuid: uuid.UUID):
        super().__init__(user, password, host, database)
        self.uuid = uuid