# ====================================
# Build the frontend
# ====================================
FROM node:22 AS frontend

WORKDIR /app/frontend

COPY frontend /app/frontend

RUN npm install && npm run build


# ====================================
# Backend
# ====================================
FROM python:3.12 AS backend

WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY backend/requirements.txt .
COPY backend/dev-requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r dev-requirements.txt

COPY --from=frontend /app/frontend/out /app/static
COPY backend/main.py .
COPY backend/app /app/app

# ====================================
# Release
# ====================================

FROM backend AS release

WORKDIR /app

# Expose the port
EXPOSE 8000

# Set environment variables
ENV PYTHONPATH=/app
ENV PORT=8000

# Start the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
