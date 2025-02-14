# Use Python 3.8 image as the base
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app directory into the container
COPY . .

# Expose the port that the app will run on
EXPOSE 5500

# Set the environment variable for Flask
ENV FLASK_APP=app.domain.update.updateSchedule

# Command to run the app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5500"]
