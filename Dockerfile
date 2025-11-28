# Use a lightweight official Python 3.9 base image
FROM python:3.9-slim-buster

# 1. Define the application's working directory inside the container.
# All subsequent commands will be executed relative to this directory.
WORKDIR /app

# 2. Copy the requirements file first to take advantage of Docker caching.
# My app needs no external packages, but it's good practice for real projects.
# COPY requirements.txt .

# 3. Copy the application code into the working directory.
# We are renaming the entry point file to main.py
COPY Anis.py main.py

# 4. Define the command that runs your application when the container starts.
# We use the exec form (square brackets) which is the preferred and safer method.
ENTRYPOINT ["python", "main.py"]
