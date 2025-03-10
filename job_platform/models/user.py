from job_platform import db
from datetime import datetime

class User(db.Model):
    """User table in database."""
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.Enum('job_seeker', 'job_provider'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
