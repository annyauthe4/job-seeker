# Job Platform

![Alt text](images/job-seeker_homepage.png)
## Overview
This project is a job platform that connects employers and job seekers. Employers can post job listings, and job seekers can browse available jobs and apply. The platform consists of a backend API built with Flask and a frontend built with HTML, CSS, and JavaScript (jQuery).

### Authors
- Salu Oluwafikunayomi <https://www.linkedin.com/in/oluwafikunayomisalu/>
- Abiodun Alagbada <https://www.linkedin.com/in/abiodunalagbada/>
- Ouwaseun Ayodele <https://www.linkedin.com/in/oluwaseun-otetumo-2b38291a5/>

## Features
- User authentication (Signup/Login)
- Role-based access control (Employers & Job Seekers)
- Employers can post job listings
- Job Seekers can view and apply for jobs
- Secure JWT-based authentication
- Responsive frontend using CSS Grid and Flexbox

## Technologies Used
### Backend:
- Flask (Python)
- Flask-JWT-Extended (for authentication)
- SQLAlchemy (ORM for database management)
- CORS (for handling cross-origin requests)

### Frontend:
- HTML
- CSS (Grid & Flexbox for layout)
- JavaScript (jQuery for AJAX requests)

### Database:
- SQLAlchemy (MySQL)

## Installation
### Prerequisites
- Python 3.x
- Flask & dependencies
- Node.js (for running frontend if needed)

### Setup Backend
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/job-platform.git
   cd job-platform
   ```
2. Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate  # For Windows
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the Flask server:
   ```sh
   flask run
   ```

### Setup Frontend
1. Open `index.html` in a browser or run using Live Server extension in VS Code.
2. Ensure the frontend is correctly making API requests to the backend.

## API Endpoints
| Method | Endpoint | Description |
|--------|------------|---------------------------|
| POST | `/api/signup/employer` | Employer signup |
| POST | `/api/signup/jobseeker` | Job Seeker signup |
| POST | `/api/login` | User login |
| POST | `/api/jobs` | Create job (Employer only) |
| GET | `/api/jobs` | Fetch all jobs (Job Seekers) |
| DELETE | `/api/jobs/<job_id>` | Delete job (Employer only) |

## Usage
### Employer Dashboard
- Employers log in and post job listings.
- Job listings are stored in the database and retrieved when needed.

### Job Seeker Dashboard
- Job seekers log in and see job listings.
- They can apply for jobs using provided links.

## Troubleshooting
### CORS Issues
- Ensure CORS is properly configured in Flask (`flask_cors` installed and enabled).

## Contributing ✍
Thank you for your interest in contributing! However, we are currently not accepting contributions.  
We will update this section once we open up for contributions. Stay tuned!

## Related Projects  
Here are some projects and tools related to this job board platform:  

- [LinkedIn Jobs](https://www.linkedin.com/jobs/) - A professional network with job listings.  
- [Indeed](https://www.indeed.com/) - A popular job search engine for job seekers.  
- [Glassdoor](https://www.glassdoor.com/) - Provides job listings along with company reviews.  
- [Job Board API](https://github.com/rdashinc/JobBoardAPI) - An open-source API for job postings.  
- [Awesome Job Boards](https://github.com/infosec-jobs/awesome-job-boards) - A curated list of job board platforms for various industries.  

## License
This project is licensed under the [MIT License](LICENSE).