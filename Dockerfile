
# Use Python as the base image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy requirements before application code
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY src/ ./src/

# Define a build argument
ARG APP_ENV=development

# Set the environment variable using the build argument
ENV APP_ENV=${APP_ENV}

# Expose the Flask application port
EXPOSE 5000

# Start the application
CMD ["python", "src/app.py"]
