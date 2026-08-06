import uuid

def random_email():
    return f"user_{uuid.uuid4().hex[:8]}@gmail.com"