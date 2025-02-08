# Use Python 3.10 as base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy only the dependencies file first (for efficient Docker caching)
COPY ../../../../requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the remaining project files into the container
COPY ../../.. /app

# Expose the port for the Create service (Change if needed)
EXPOSE 5001

# Command to run the Create service
CMD ["python", "/app/app/domain/create/main.py"]
