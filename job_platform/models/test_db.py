#!/usr/bin/python3

from job_platform.models.engine.db_storage import DBStorage
from job_platform.models.user import User
from job_platform.models.employer import Employer
from job_platform.models.job import Job

"""
new_job = Job(
    job_title="Social worker",
    description="Save the children",
    location="UK",
    company='Unicef',
    salary=12000,
    website_link="https://example.com/job-apply",
    employer_id='ea021643-8b22-4f7f-bcaf-23839ebad61f'
)


employer = Employer(
    full_name="Ore-Oluwa Adetola",
    email="ore@gmail.com",
    password="complexpassword",
    company_name="Save Humanity Ltd.",
    website="https://savehumanity.com"
)
"""

storage = DBStorage()
storage.reload()
all_data = storage.all(User)
user = None
for items in all_data.values():
    if "fikun@gmail.com" == items.email:
        user = items
print(user.email)
