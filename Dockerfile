FROM python:3.9-slim

# Set environment variables to prevent Python from writing pyc files to disc (PYTHONDONTWRITEBYTECODE)
# and buffering stdout and stderr (PYTHONUNBUFFERED)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /usr/src/app

# Install system dependencies (if you have any OS-level deps)
RUN apt-get update && apt-get install -y --no-install-recommends \
    # build-essential libpq-dev can be included if needed for packages with C extensions
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY Pipfile Pipfile.lock /usr/src/app/
# Install the dependencies system-wide, include gunicorn in the Pipfile or install it explicitly here
RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile

# Install gunicorn separately if it's not included in your Pipfile
RUN pip install gunicorn

# Copy project files to the container
COPY . /usr/src/app/

# Expose the port the app runs on
EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "rakt_challenge.wsgi:application"]
