import bcrypt


def hash_password(password: str) -> str:
    password = password.encode()
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password, salt).decode()


def validate_password(user_password: str, hashed_passowrd: str) -> bool:
    user_password: bytes = user_password.encode()
    hashed_passowrd: bytes = hashed_passowrd.encode()
    return bcrypt.checkpw(user_password, hashed_passowrd)


if __name__ == '__main__':
    passw: str = hash_password("pass123")
    print(passw)

    print(validate_password("pass123", passw))
