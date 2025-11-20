# Use official Python
FROM python:3.10-slim

# Disable Python buffering
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Create working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port for Cloud Run
EXPOSE 8080

# Run Django via Gunicorn
CMD ["gunicorn", "--bind", ":8080", "core.wsgi:application"]
