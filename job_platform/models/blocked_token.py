#!/usr/bin/python3
"""
Sets up a table for black listed tokens
"""
from job_platform.models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey


class BlockedToken(BaseModel):
    """Creates a table to store black listed tokens"""
    __tablename__ = 'blockedtokens'

    id = Column(String(36), primary_key=True, unique=True, nullable=False)
