FROM python:3.11-slim

# Install Node.js for markdown lint tasks
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y curl gnupg && \
    curl -fsSL https://deb.nodesource.com/setup_18.x -o /tmp/nodesource.sh && \
    bash /tmp/nodesource.sh && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y nodejs && rm -rf /var/lib/apt/lists/* /tmp/nodesource.sh

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
