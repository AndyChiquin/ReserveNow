# Use Python as base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy all necessary files
COPY ../../.. /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for the Read service
EXPOSE 5004

# Command to run the Read service
CMD ["python", "app/domain/read/read.py"]
