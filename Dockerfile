# Use python:3.9-slim as the base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Environment variables for production (provide API keys at runtime)
ENV FLASK_ENV=production
ENV PORT=8000

# Expose the port the app runs on
EXPOSE 8000

# Set the entry point to run the Flask app
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
