FROM python:3.11-slim

# Install Node.js for markdown lint tasks
RUN apt-get update && apt-get install -y curl gnupg && \
    curl -fsSL https://deb.nodesource.com/setup_18.20.0 -o /tmp/nodesource.sh && \
    echo "ed44586adc96bd3e7707abe7659d585dd2e78c67d779bd175273b99bd07a099e  /tmp/nodesource.sh" | sha256sum -c - && \
    bash /tmp/nodesource.sh && \
    apt-get install -y nodejs && rm -rf /var/lib/apt/lists/* /tmp/nodesource.sh

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
