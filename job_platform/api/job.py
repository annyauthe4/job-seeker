"""
This module defines the api for posting job and uploading file.
"""
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from job_platform import db
from job_platform.models.job import Job, JobProvider, JobSeeker
import os

job_api = Blueprint('job_api', __name__)

@job_api.route('/upload_cv', methods=['POST'])
@jwt_required()
def upload_cv():
    """CV upload method."""
    user = get_jwt_identity()
    if user["role"] != "job_seeker":
        return jsonify({"error": "Unauthorized"}), 403

    file = request.files['cv']
    if file:
        filename = f"cv_{user['id']}.pdf"
        file_path = os.path.join("uploads", filename)
        file.save(file_path)
        
        job_seeker = JobSeeker.query.filter_by(user_id=user["id"]).first()
        job_seeker.cv_filename = filename
        db.session.commit()
        return jsonify({"message": "CV uploaded successfully"}), 200

    return jsonify({"error": "No file uploaded"}), 400


@job_api.route('/post_job', methods=['POST'])
@jwt_required()
def post_job():
    """Job posting method."""
    user = get_jwt_identity()
    if user["role"] != "job_provider":
        return jsonify({"error": "Unauthorized"}), 403

    data = request.json
    title = data['title']
    description = data['description']

    provider = JobProvider.query.filter_by(user_id=user["id"]).first()
    job = Job(provider_id=provider.id, title=title, description=description)

    db.session.add(job)
    db.session.commit()
    return jsonify({"message": "Job posted successfully"}), 201
