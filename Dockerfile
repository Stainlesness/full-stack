# Stage 1: Build the frontend
FROM node:16-alpine as frontend-build

# Set working directory
WORKDIR /frontend

# Copy frontend package.json and package-lock.json
COPY frontend--main/package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the frontend code
COPY frontend--main/ .

# Build the frontend
RUN npm run build

# Stage 2: Build the backend and combine with frontend
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy backend requirements file
COPY backend-main/requirements.txt .

# Install backend dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend-main/ .

# Copy built frontend code from the previous stage
COPY --from=frontend-build /frontend/dist ./app/static

# Expose the port the backend runs on
EXPOSE 5000

# Command to run the backend server
CMD ["python", "run.py"]
