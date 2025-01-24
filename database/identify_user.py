"""This module contains code to identify users between sessions."""

import mysql.connector
import os
import uuid
import json
from dotenv import load_dotenv

def open_connection():
    """Open a MySQL connection."""
    mydb = mysql.connector.connect()