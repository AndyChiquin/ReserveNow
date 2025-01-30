# Use a lightweight Python image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy the service files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port where Flask will run
EXPOSE 5000

# Command to run the service
CMD ["python", "main.py"]
