FROM python:3.12-slim

# Prevent Python from writing pyc files to disk and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies (build-essential often needed for compiling stats/science packages)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app/

# Install the project and its dev dependencies
RUN pip install --upgrade pip && \
    pip install -e .[dev]

# Expose ports for future visualization (Plotly) and API (FastAPI) layers
EXPOSE 8050
EXPOSE 8000

# Default command runs the test suite
CMD ["pytest", "tests/"]
