FROM python:3.11-slim

# Install Node.js for markdown lint tasks
RUN apt-get update && apt-get install -y curl gnupg && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy dependency files first for caching
COPY pyproject.toml requirements*.txt ./
COPY package*.json ./

# Install Python and Node dependencies
RUN pip install --no-cache-dir -r requirements.txt \
    && if [ -f requirements-dev.txt ]; then pip install --no-cache-dir -r requirements-dev.txt; fi \
    && if [ -f package.json ]; then npm ci --omit=optional; fi

# Copy source code
COPY . .

CMD ["python", "examples/simple_workflow.py"]
