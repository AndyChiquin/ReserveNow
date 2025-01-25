# Use an official Node.js base image
FROM node:16

# Set the working directory inside the container
WORKDIR /app

# Copy the files needed to install dependencies
COPY package.json package-lock.json ./

# Install the dependencies
RUN npm install

# Copy the rest of the files to the container
COPY . .

# Expose the port your microservice runs on
EXPOSE 3000

# Command to start the application
CMD [“node”, “src/app.js”]

