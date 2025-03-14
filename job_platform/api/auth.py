from flask import Blueprint, request, jsonify
from job_platform import db
from job_platform.models.user import User
from job_platform.models.job import JobSeeker, JobProvider
from job_platform.utils.security import hash_password, check_password
from flask_jwt_extended import create_access_token

auth_api = Blueprint('auth_api', __name__)


@auth_api.route('/signup', methods=['POST'])
def signup():
    """User signup method."""
    data = request.json
    full_name = data['full_name']
    email = data['email']
    password = data['password']
    role = data['role']

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already exists"}), 400

    user = User(full_name=full_name, email=email,
                password=hash_password(password), role=role)
    db.session.add(user)
    db.session.commit()

    if role == 'job_seeker':
        db.session.add(JobSeeker(user_id=user.id))
    elif role == 'job_provider':
        db.session.add(JobProvider(user_id=user.id))

    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201


@auth_api.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data['email']
    password = data['password']

    user = User.query.filter_by(email=email).first()
    if not user or not check_password(user.password, password):
        return jsonify({"error": "Invalid email or password"}), 401

    access_token = create_access_token(
                                       identity={
                                           "id": user.id,
                                           "role": user.role})
    return jsonify({"access_token": access_token}), 200
