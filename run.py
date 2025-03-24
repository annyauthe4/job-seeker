#!/usr/bin/python3
"""Module for running application."""
from job_platform import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
