# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variable for the GEMINI_API_KEY (you can set this dynamically later)
ENV GEMINI_API_KEY=your_api_key_here

# Command to run the script when the container starts
CMD ["python", "App.py"]
