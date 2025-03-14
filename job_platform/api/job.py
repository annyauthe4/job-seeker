#!/usr/bin/python3
from flask import Blueprint, request, jsonify
from job_platform.models.engine.db_storage import db
from job_platform.models.job import Job
from job_platform.models.user import User
from job_platform.models.job_seeker import JobSeeker
from job_platform.models.employer import Employer
from flask_jwt_extended import jwt_required, get_jwt_identity

job_api = Blueprint('job_api', __name__)


@job_api.route('/jobs', methods=['GET'])
def get_jobs():
    """Retrieve all job listings."""
    jobs = Job.query.all()
    return jsonify([job.to_dict() for job in jobs]), 200


@job_api.route('/jobs/<int:job_id>', methods=['GET'])
def get_job(job_id):
    """Retrieve a single job by ID."""
    job = Job.query.get(job_id)
    if not job:
        return jsonify({"error": "Job not found"}), 404
    return jsonify(job.to_dict()), 200


@job_api.route('/jobs', methods=['POST'])
@jwt_required()
def post_job():
    """Post a new job (Employer only."""
    user_identity = get_jwt_identity()
    user = User.query.get(user_identity["id"])

    if not isinstance(user, Employer):
        return jsonify({"error":
                        "Only employers can post jobs"}), 403

    data = request.json
    required_fields = ["job_title", "description",
                       "location", "company", "salary"]
    if not all(field in data for field in required_fields):
        return jsonify({"error":
                        "Missing required fields"}), 400

    new_job = Job(
        job_title=data['job_title'],
        description=data['description'],
        location=data['location'],
        company=data['company'],
        salary=data.get('salary'),
        website_link=data.get('website_link', ''),
        employer_id=user.id
    )
    db.session.add(new_job)
    db.session.commit()
    return jsonify({"message": "Job created successfully",
                    "job": new_job.to_dict()}), 201


@job_api.route('/jobs/<int:job_id>', methods=['PUT'])
@jwt_required()
def update_job(job_id):
    """Update an existing job listing."""
    job = Job.query.get(job_id)
    if not job:
        return jsonify({"error": "Job not found"}), 404

    data = request.json
    for key, value in data.items():
        if hasattr(job, key):
            setattr(job, key, value)

    db.session.commit()
    return jsonify({"message": "Job updated successfully",
                    "job": job.to_dict()}), 200


@job_api.route('/jobs/<int:job_id>', methods=['DELETE'])
@jwt_required()
def delete_job(job_id):
    """Delete a job listing."""
    job = Job.query.get(job_id)
    if not job:
        return jsonify({"error": "Job not found"}), 404

    db.session.delete(job)
    db.session.commit()
    return jsonify({"message": "Job deleted successfully"}), 200


@job_api.route('/upload_cv', methods=['POST'])
@jwt_required()
def upload_cv():
    """Upload CV (Job Seeker only)."""
    user_identity = get_jwt_identity()
    user = User.query.get(user_identity["id"])

    if not isinstance(user, JobSeeker):
        return jsonify({"error":
                        "Only job seekers can upload CVs"}), 403

    if 'cv' not in request.files:
        return jsonify({"error": "No CV file provided"}), 400

    cv_file = request.files['cv']
    if cv_file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save the file
    file_path = f"uploads/cvs/{user.id}_{cv_file.filename}"
    cv_file.save(file_path)

    user.cv_link = file_path
    db.session.commit()

    return jsonify({"message":
                    "CV uploaded successfully",
                    "cv_link": file_path}), 200
