# Use Python 3.10 as base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy only the dependencies file first (for efficient Docker caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the remaining project files into the container
COPY . .

# Expose the port for the readSpecialDay service
EXPOSE 5401  

# Command to run the readSpecialDay service
CMD ["python", "-m", "domain.read.main"]
