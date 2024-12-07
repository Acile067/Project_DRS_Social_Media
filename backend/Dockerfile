# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /project

# Copy only requirements first for better caching
COPY requirements.txt /project/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /project/

# Expose the application port
EXPOSE 5000

# Run the application
CMD ["python", "run.py"]
