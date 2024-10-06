# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /

# Copy the current directory contents into the container at /app
COPY . /

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set the default command to run the application
CMD ["python", "src/main.py"]
