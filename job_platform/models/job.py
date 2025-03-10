from job_platform import db
from datetime import datetime


class JobSeeker(db.Model):
    """Job seeker class."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    cv_filename = db.Column(db.String(255), nullable=True)


class JobProvider(db.Model):
    """Job Provider class."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class Job(db.Model):
    """Job with its attributes."""
    id = db.Column(db.Integer, primary_key=True)
    provider_id = db.Column(db.Integer, db.ForeignKey('job_provider.id'),
                            nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
