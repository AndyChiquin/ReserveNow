# Use Python 3.10 as base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy only the dependencies file first (for efficient Docker caching)
COPY ../../../../requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into the container
COPY ../../.. /app

# Expose the port for the Delete service
EXPOSE 5004

# Command to run the Delete service
CMD ["python", "/app/app/domain/delete/main.py"]
