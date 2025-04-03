#!/bin/bash

# Exit on error
set -e

# Configuration
AWS_REGION="us-west-2"
ECR_REPO_NAME="aiops-guardian"
K8S_NAMESPACE="aiops-guardian"

# Get AWS account ID
AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
ECR_REPO_URI="${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO_NAME}"

# Create ECR repository if it doesn't exist
aws ecr describe-repositories --repository-names ${ECR_REPO_NAME} || \
aws ecr create-repository --repository-name ${ECR_REPO_NAME}

# Login to ECR
aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${ECR_REPO_URI}

# Build and push frontend image
echo "Building frontend image..."
docker build -t ${ECR_REPO_URI}-frontend:latest -f docker/frontend/Dockerfile frontend/
docker push ${ECR_REPO_URI}-frontend:latest

# Build and push backend image
echo "Building backend image..."
docker build -t ${ECR_REPO_URI}-backend:latest -f docker/backend/Dockerfile backend/
docker push ${ECR_REPO_URI}-backend:latest

# Create namespace if it doesn't exist
kubectl create namespace ${K8S_NAMESPACE} --dry-run=client -o yaml | kubectl apply -f -

# Create AWS credentials secret
kubectl create secret generic aws-credentials \
  --namespace ${K8S_NAMESPACE} \
  --from-literal=AWS_ACCESS_KEY_ID=$(aws configure get aws_access_key_id) \
  --from-literal=AWS_SECRET_ACCESS_KEY=$(aws configure get aws_secret_access_key) \
  --from-literal=AWS_REGION=${AWS_REGION} \
  --dry-run=client -o yaml | kubectl apply -f -

# Deploy using Helm
echo "Deploying using Helm..."
helm upgrade --install aiops-guardian ./helm/aiops-guardian \
  --namespace ${K8S_NAMESPACE} \
  --set frontend.image.repository=${ECR_REPO_URI}-frontend \
  --set backend.image.repository=${ECR_REPO_URI}-backend \
  --set global.region=${AWS_REGION}

# Wait for deployments to be ready
echo "Waiting for deployments to be ready..."
kubectl wait --for=condition=available deployment/aiops-guardian-frontend -n ${K8S_NAMESPACE} --timeout=300s
kubectl wait --for=condition=available deployment/aiops-guardian-backend -n ${K8S_NAMESPACE} --timeout=300s

echo "Deployment completed successfully!" 