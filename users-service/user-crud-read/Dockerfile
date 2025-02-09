# Use an optimized Go base image
FROM golang:1.19-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy dependencies and install required packages
COPY go.mod go.sum ./
RUN go mod download

# Copy the entire project into the container
COPY . .

# Expose port 8006 (same as configured in Go)
EXPOSE 8007

# Command to start the server
CMD ["go", "run", "src/server.go"]
