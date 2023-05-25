# Use the official Python base image for Python 3.7
FROM python:3.7-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files to the working directory
COPY main.py .
COPY test.py .
COPY data.csv .

# Expose the port on which the FastAPI server will run
EXPOSE 8000

# Start the FastAPI server
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0","--port","8000","--reload"]
