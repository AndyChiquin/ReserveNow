# Use Python as base image
FROM python:3.9

# Set working directory
WORKDIR /app

COPY ../../.. /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for the Create service
EXPOSE 5003

# Command to run the Create service
CMD ["python", "app/domain/create/create.py"]
