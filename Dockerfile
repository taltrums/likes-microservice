# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# expose the port 5000
EXPOSE 5000

# Set the command to run the Flask application
CMD [ "flask", "run", "--host=0.0.0.0", "--port=5000"]
