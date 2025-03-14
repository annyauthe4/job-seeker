"""
This is where password is hashed(encrypted) and checked
"""
from job_platform import bcrypt


def hash_password(password):
    """Method for encrypting user password."""
    return bcrypt.generate_password_hash(password).decode("utf-8")


def check_password(hashed_password, password):
    """Method for checking user password."""
    return bcrypt.check_password_hash(hashed_password, password)
