# AIOps Guardian

```
    █████╗ ██╗ ██████╗ ██████╗ ███████╗    ██████╗ ██╗   ██╗ █████╗ ██████╗ ██████╗ ██╗ ██████╗ ███╗   ██╗
   ██╔══██╗██║██╔════╝██╔═══██╗██╔════╝    ██╔══██╗██║   ██║██╔══██╗██╔══██╗██╔══██╗██║██╔═══██╗████╗  ██║
   ███████║██║██║     ██║   ██║███████╗    ██████╔╝██║   ██║███████║██████╔╝██║  ██║██║██║   ██║██╔██╗ ██║
   ██╔══██║██║██║     ██║   ██║╚════██║    ██╔══██╗██║   ██║██╔══██║██╔══██╗██║  ██║██║██║   ██║██║╚██╗██║
   ██║  ██║██║╚██████╗╚██████╔╝███████║    ██║  ██║╚██████╔╝██║  ██║██║  ██║██████╔╝██║╚██████╔╝██║ ╚████║
   ╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═════╝ ╚══════╝    ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
```

```
   ╔════════════════════════════════════════════════════════════════════════════════════════════════════════╗
   ║                                                                                                        ║
   ║  🛡️  Guardian Shield: Protecting your infrastructure with AI-powered insights and automated operations  ║
   ║                                                                                                        ║
   ╚════════════════════════════════════════════════════════════════════════════════════════════════════════╝
```

A comprehensive AIOps platform that leverages AWS Bedrock for intelligent incident management, root cause analysis, and automated operations.

## System Architecture

```mermaid
graph TD
    A[Frontend] --> B[Backend API]
    B --> C[Multi-Agent System]
    C --> D[Log Analyzer]
    C --> E[Metric Analyzer]
    C --> F[Dashboard Analyzer]
    B --> G[Knowledge Base]
    B --> H[AWS Bedrock]
    B --> I[Monitoring]
```

## Deployment Architecture

```mermaid
graph LR
    A[Developer] --> B[deploy.sh]
    B --> C[Build Docker Images]
    C --> D[Push to ECR]
    D --> E[Deploy to EKS]
    E --> F[Frontend Pod]
    E --> G[Backend Pod]
    F --> H[ALB Ingress]
    G --> H
```

## Component Interaction

```mermaid
sequenceDiagram
    participant U as User
    participant F as Frontend
    participant B as Backend
    participant A as Agents
    participant K as Knowledge Base
    participant M as AWS Bedrock

    U->>F: Access Dashboard
    F->>B: Request Data
    B->>A: Trigger Analysis
    A->>K: Query Knowledge Base
    A->>M: Get AI Insights
    M-->>A: Return Analysis
    A-->>B: Combine Results
    B-->>F: Send Response
    F-->>U: Display Results
```

## Infrastructure Components

```mermaid
graph TD
    A[VPC] --> B[Public Subnets]
    A --> C[Private Subnets]
    C --> D[EKS Cluster]
    D --> E[Node Groups]
    B --> F[ALB]
    F --> G[Ingress Controller]
    G --> D
```

## GitOps Workflow with ArgoCD

```mermaid
graph LR
    A[Git Repository] --> B[ArgoCD]
    B --> C[Helm Charts]
    C --> D[Kubernetes Cluster]
    B --> E[Sync Status]
    E --> A
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#bfb,stroke:#333,stroke-width:2px
```

## Helm Chart Structure

```mermaid
graph TD
    A[Helm Chart] --> B[Values]
    A --> C[Templates]
    A --> D[Charts]
    C --> E[Deployment]
    C --> F[Service]
    C --> G[Ingress]
    C --> H[ConfigMap]
    C --> I[Secret]
    B --> J[Default Values]
    B --> K[Environment Values]
```

## Anomaly Detection Flow

```mermaid
graph TD
    A[Metrics Collection] --> B[Data Preprocessing]
    B --> C[Statistical Analysis]
    C --> D[ML Models]
    D --> E[Anomaly Detection]
    E --> F[Alert Generation]
    F --> G[Incident Creation]
    G --> H[Root Cause Analysis]
    H --> I[Resolution]
    
    subgraph "Real-time Monitoring"
    A
    end
    
    subgraph "Analysis Pipeline"
    B
    C
    D
    E
    end
    
    subgraph "Response"
    F
    G
    H
    I
    end
```

## Features

- Multi-agent system for incident management
- AWS Bedrock integration for AI-powered insights
- Knowledge base for historical incident data
- Multi-modal analysis of logs, metrics, and dashboards
- Grafana dashboard integration
- Real-time incident response
- Root cause analysis automation
- Anomaly detection and alerting
- Automated incident resolution
- Predictive maintenance

## Project Structure

```
.
├── frontend/           # React.js frontend application
├── backend/           # FastAPI backend service
├── infrastructure/    # Terraform configurations
├── docker/           # Docker configurations
├── agents/           # Multi-agent system
├── knowledge_base/   # Knowledge base and historical data
├── monitoring/       # Monitoring and visualization
├── helm/            # Helm charts
└── argocd/          # ArgoCD configurations
```

## Prerequisites

- Node.js >= 16
- Python >= 3.9
- Docker
- AWS CLI configured
- Terraform >= 1.0
- kubectl

## Setup Instructions

1. Clone the repository
2. Install dependencies:
   ```bash
   # Frontend
   cd frontend
   npm install

   # Backend
   cd backend
   python -m venv venv
   source venv/bin/activate  # or `venv\Scripts\activate` on Windows
   pip install -r requirements.txt
   ```

3. Configure AWS credentials:
   ```bash
   aws configure
   ```

4. Deploy infrastructure:
   ```bash
   cd infrastructure
   terraform init
   terraform plan
   terraform apply
   ```

5. Deploy ArgoCD:
   ```bash
   # Install ArgoCD CLI
   brew install argocd  # macOS
   # or
   curl -sSL -o /usr/local/bin/argocd https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64
   chmod +x /usr/local/bin/argocd

   # Install ArgoCD in the cluster
   kubectl create namespace argocd
   kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

   # Wait for ArgoCD to be ready
   kubectl wait --for=condition=ready pod -l app.kubernetes.io/name=argocd-server -n argocd --timeout=300s

   # Get ArgoCD admin password
   argocd admin initial-password -n argocd
   ```

6. Deploy application using ArgoCD:
   ```bash
   # Login to ArgoCD
   argocd login argocd-server

   # Create the application
   kubectl apply -f argocd/applications/sre-copilot.yaml

   # Monitor the deployment
   argocd app get sre-copilot
   ```

7. Manual deployment (alternative):
   ```bash
   # Build and push Docker images
   ./docker/build.sh

   # Deploy using Helm
   helm upgrade --install sre-copilot ./helm/sre-copilot \
     --namespace sre-copilot \
     --create-namespace \
     --set frontend.image.repository=${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/sre-copilot-frontend \
     --set backend.image.repository=${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/sre-copilot-backend
   ```

## Development

1. Start frontend development server:
   ```bash
   cd frontend
   npm start
   ```

2. Start backend development server:
   ```bash
   cd backend
   uvicorn main:app --reload
   ```

## License

MIT 