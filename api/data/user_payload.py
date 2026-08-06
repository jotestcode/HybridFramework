from api.utils.random_data import random_email

def create_user_payload():
    return {
        "name": "Emma Watson",
        "gender": "female",
        "email": random_email(),
        "status": "active"
    }