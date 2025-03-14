from flask import Blueprint, request, jsonify
from job_platform.models.engine.db_storage import db
from job_platform.models.user import User
from job_platform.models.job_seeker import JobSeeker
from job_platform.models.employer import Employer
from job_platform.utils.security import hash_password, check_password
from flask_jwt_extended import create_access_token

auth_api = Blueprint('auth_api', __name__)


@auth_api.route('/signup', methods=['POST'])
def signup():
    """User signup method."""
    data = request.json

    # Validate required fields
    required_fields = ['full_name', 'email', 'password', 'role']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    full_name = data.get('full_name')
    email = data.get('email')
    password = data.get('password')
    role = data.get('role')

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already exists"}), 400

    # Create user and hash password
    user = User(full_name=full_name, email=email,
                password=hash_password(password), role=role)
    db.session.add(user)
    db.session.commit()  # Ensure the user is saved first

    # Create related profile
    if role == 'job_seeker':
        job_seeker = JobSeeker(user_id=user.id)
        db.session.add(job_seeker)
    elif role == 'employer':
        employer = Employer(user_id=user.id)
        db.session.add(employer)

    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201


@auth_api.route('/login', methods=['POST'])
def login():
    """User login method."""
    data = request.json

    # Validate required fields
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({"error": "Missing email or password"}), 400

    email = data.get('email')
    password = data.get('password')

    # Check if user exists
    user = User.query.filter_by(email=email).first()
    if not user or not check_password(password, user.password):
        return jsonify({"error": "Invalid email or password"}), 401

    # Generate JWT access token
    access_token = create_access_token(
                       identity={"id": user.id,
                                 "role": user.role})

    return jsonify({"access_token": access_token}), 200
