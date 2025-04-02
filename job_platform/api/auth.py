#!/usr/bin/python3
# The module sets up the routes in the flask app

from flask import Blueprint, request, jsonify, abort, render_template
from job_platform.models.engine.db_storage import DBStorage
from job_platform.models.user import User
from job_platform.models.job_seeker import JobSeeker
from job_platform.models.employer import Employer
from job_platform.utils.security import hash_password, check_password
from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from job_platform.models.blocked_token import BlockedToken

auth_api = Blueprint('auth_api', __name__)
storage = DBStorage()  # Instance of the database storage
storage.reload()


@auth_api.route('/')
def landing_page():
    """Site landing page."""
    return render_template('landing.html')


# Set up sign up for Employers
@auth_api.route('/signup/employer', methods=['POST'])
def signupEmployer():
    """User signup method."""
    data = request.json

    if not data:
        return jsonify({"error": "Data was not given"})
    # Validate required fields
    required_fields = ['full_name', 'email', 'password', 'company_name']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    full_name = data.get('full_name')
    email = data.get('email')
    password = data.get('password')
    company_name = data.get('company_name')
    website = data.get('website', '')

    all_data = storage.all(User)
    for items in all_data.values():
        if email == items.to_dict().get('email'):
            return jsonify({"error": "Email already exists"}), 400
    # Create a new employer
    employer = Employer(
            full_name=full_name,
            email=email,
            password=hash_password(password),
            company_name=company_name,
            website=website
            )
    storage.new(employer)
    storage.save()
    return jsonify({
        "message": "Employer signed up!",
        "role": "employer"
    }), 201


# Set up sign up for Job seekers
@auth_api.route('/signup/jobseeker', methods=['POST'])
def signupJobSeeker():
    """User signup method."""
    data = request.json

    if not data:
        return jsonify({"error": "Data was not given"})
    # Validate required fields
    required_fields = ['full_name', 'email', 'password']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    full_name = data.get('full_name')
    email = data.get('email')
    password = data.get('password')
    cv_link = data.get('cv_link', '')

    all_data = storage.all(User)
    for items in all_data.values():
        if email == items.to_dict().get('email'):
            return jsonify({"error": "Email already exists"}), 400
    # Create a new job_seeker
    seeker = JobSeeker(
            full_name=full_name,
            email=email,
            password=hash_password(password),
            cv_link=cv_link
            )
    storage.new(seeker)
    storage.save()
    return jsonify({
        "message": "You are all signed up!",
        "role": "jobseeker"
    }), 201


# Set up login for all users
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
    user = None

    all_data = storage.all(User)
    for items in all_data.values():
        if email == items.email:
            user = items
            break
    print(user)
    if not user or not check_password(user.password, password):
        return jsonify({"error": "Invalid email or password"}), 401

    # Generate JWT access token
    access_token = create_access_token(
                       identity={"id": user.id,
                                 "role": user.role})

    return jsonify({"access_token": access_token}), 200


@auth_api.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    """ When a user logs out of the application
        the users current access token is stored
    """
    jti = get_jwt()['jti']
    blocked_token = BlockedToken(id=jti)  # Blacklist token

    storage.new(blocked_token)
    storage.save()

    return jsonify({"msg": "Successfully logged out."}), 200
