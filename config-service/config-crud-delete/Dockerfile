# Use an optimized Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy dependencies and install required packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose port 8004 (same as configured in FastAPI)
EXPOSE 8004

# Command to start the FastAPI server
CMD ["uvicorn", "src.server:app", "--host", "0.0.0.0", "--port", "8004"]
