### Network Security Project For Phising Data
This project is an end-to-end Machine Learning pipeline designed to detect phishing attempts using classification techniques. It follows a modular and production-grade architecture, integrating data ingestion, model training, experiment tracking, and deployment.

```

```
### ML App Overview:

The goal of this project is to classify whether a given input (e.g., URL, email features, etc.) is phishing or legitimate using machine learning models.

The system is built with:

Scalable architecture (config → components → artifacts)
Experiment tracking using MLflow
Cloud integration with MongoDB & AWS S3
Containerization using Docker and AWS ECR
API deployment using FastAPI
CI/CD Pipeline
AWS EC2 deployment

```

```
### Project Architecture

The project follows a structured pipeline:

Project
│── config/              # Configuration files
│── components/          # ML pipeline components
│── artifacts/           # Generated outputs (models, data, etc.)
│── logs/                # Logging files
│── src/                 # Core source code
│── app.py               # FastAPI application
│── Dockerfile           # Docker configuration
│── requirements.txt     # Dependencies
│── setup.py             # Package setup

```

```
### 1. Environment & Dependency Setup
setup.py for packaging the project
requirements.txt for managing dependencies

```

```
### 2. Data Ingestion (MongoDB)
Raw dataset in .csv format
Script: push_data.py
Uses .env file for secure MongoDB connection

Environment Variable:

MONGO_DB_URL=your_mongodb_connection_string

```

```
### 3. Modular Pipeline Design
Configuration-driven architecture
Separate components for:
Data ingestion
Data validation
Data transformation
Model training
Model evaluation

```

```
### 4. Logging System
Custom logger implemented
Tracks:
Pipeline execution
Errors
Debug information

```

```
### 5. Experiment Tracking (MLflow)
Tracks:
Model parameters
Metrics
Artifacts
Model registry for version control

```

```
### 6. AWS S3 Integration
File: s3_syncer.py
Syncs local artifacts and final model with S3 bucket
Enables:
Model storage
Artifact versioning
Cloud backup

```

```
### 7. Docker Support
Dockerfile created for containerization
Ensures reproducibility across environments

```

```
### 8. FastAPI Deployment
File: app.py
Provides API endpoints for:
Model inference
Health checks

Run locally:

uvicorn app:app --reload

```

```
### 9. CI/CD Pipeline (GitHub Actions + AWS)
Implemented CI/CD using a .yml workflow file (GitHub Actions)
Automatically builds and pushes Docker images to Amazon ECR (Private Repository) after code changes
Configured self-hosted runner on EC2 for continuous deployment
Enables:
Automated build → test → push → deploy cycle
Faster and consistent production updates
Reduced manual intervention

Workflow Summary:

Code pushed to GitHub
GitHub Actions triggers pipeline
Docker image is built
Image pushed to ECR
EC2 self-runner pulls latest image
Application is redeployed automatically

```

```
### 10. Installation & Setup
1. Clone Repository
git clone https://github.com/your-username/phishing-detection-ml.git
cd phishing-detection-ml

```

```
2. Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

```

```
3. Install Dependencies
pip install -r requirements.txt

```

```
4. Setup Environment Variables

Create .env file:

MONGO_DB_URL=your_connection_string

```

```
# Run with Docker
docker build -t mlapp .
docker run -p 8000:8000 mlapp

```

```
# API Usage

Once running:

http://127.0.0.1:8000/docs

```

```
Setup github secrets:
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = 

AWS_ECR_LOGIN_URI = 
ECR_REPOSITORY_NAME = 


Docker Setup In EC2 commands to be Executed

#optional

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

```
