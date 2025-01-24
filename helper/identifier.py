import uuid
from dotenv import load_dotenv, set_key
import os

def generate_id():
    return str(uuid.uuid4())

def get_or_create_identifier():
    user_uuid = os.getenv("USER_UUID")
    if not user_uuid:
        user_uuid = generate_id()
        set_key("../.env","USER_UUID", user_uuid)
    return user_uuid
