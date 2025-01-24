import uuid
from dotenv import set_key
import os

def generate_id():
    return str(uuid.uuid4())

def get_or_create_identifier():
    # TODO: fix error where 'set_key' isn't writing to the .env file
    user_uuid = os.getenv("USER_UUID")
    if not user_uuid:
        user_uuid = generate_id()
        set_key("../.env","USER_UUID", user_uuid)
        print("UUID written to .env")
    return user_uuid
