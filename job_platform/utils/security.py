#!/usr/bin/python3
"""Security utilities."""
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, decode_token
from datetime import timedelta
import os

# Set token expiration time (e.g., 1 hour)
TOKEN_EXPIRATION = timedelta(hours=1)


def hash_password(password):
    """
    Hashes a password securely using PBKDF2.
    :param password: Plain text password.
    :return: Hashed password.
    """
    return generate_password_hash(password)


def check_password(hashed_password, password):
    """
    Verifies a password against its hash.
    :param hashed_password: Stored hashed password.
    :param password: Plain text password for verification.
    :return: True if password matches, False otherwise.
    """
    return check_password_hash(hashed_password, password)


def generate_jwt(user):
    """
    Generates a JWT token for authentication.
    :param user: User object (must have 'id' and 'role' attributes).
    :return: JWT token.
    """
    payload = {
        "id": user.id,
        "role": user.role
    }
    return create_access_token(identity=payload,
                               expires_delta=TOKEN_EXPIRATION)


def decode_jwt(token):
    """
    Decodes a JWT token and retrieves user identity.
    :param token: JWT token string.
    :return: Decoded token data or None if invalid.
    """
    try:
        return decode_token(token)["sub"]
    except Exception:
        return None
