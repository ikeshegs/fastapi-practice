from jose import JWTError, jwt
from datetime import datetime, timedelta

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "7b82bfb07005ff9e636353a2835bcc19c87398c5cc0fff5a4fb0372c99ba1e60"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt
