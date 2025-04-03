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

## Step Functions Workflow

```mermaid
graph TD
    A[Detect Anomaly] --> B{Check Severity}
    B -->|Critical| C[Create Critical Incident]
    B -->|High| D[Create High Priority Incident]
    B -->|Medium| E[Create Medium Priority Incident]
    B -->|Low| F[Log Low Severity]
    
    C --> G[Trigger Immediate Response]
    G --> H[Analyze Root Cause]
    D --> H
    
    H --> I[Generate Resolution Plan]
    I --> J[Execute Resolution]
    J --> K[Verify Resolution]
    K --> L[Update Incident Status]
    L --> M[Generate Report]
    
    E --> N[Schedule Analysis]
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#f66,stroke:#333,stroke-width:2px
    style D fill:#f96,stroke:#333,stroke-width:2px
    style E fill:#ff9,stroke:#333,stroke-width:2px
    style F fill:#9f9,stroke:#333,stroke-width:2px
```

## AWS Step Functions Integration

```mermaid
graph TD
    subgraph "AWS CloudWatch"
        A[Metrics] --> B[CloudWatch Alarms]
        C[Logs] --> D[Log Groups]
        E[Custom Metrics] --> F[Metric Streams]
        G[Log Insights] --> H[Log Analytics]
    end

    subgraph "AWS EventBridge"
        I[Event Bus] --> J[Rules]
        J --> K[Scheduled Events]
        J --> L[Event Patterns]
        M[API Destinations]
    end

    subgraph "AWS Step Functions"
        N[State Machine] --> O[Lambda Functions]
        O --> P[Choice States]
        P --> Q[Task States]
    end

    subgraph "AWS Lambda Functions"
        R[Anomaly Detection]
        S[Incident Creation]
        T[Root Cause Analysis]
        U[Resolution Planning]
        V[Resolution Execution]
        W[Verification]
    end

    subgraph "AWS Services"
        X[AWS Bedrock]
        Y[Amazon S3]
        Z[DynamoDB]
        AA[SNS Topics]
    end

    B --> N
    D --> N
    F --> N
    H --> N
    
    K --> N
    L --> N
    
    N --> R
    R --> S
    S --> T
    T --> U
    U --> V
    V --> W
    
    R --> X
    T --> X
    U --> X
    
    S --> Z
    W --> Z
    
    V --> Y
    W --> Y
    
    S --> AA
    V --> AA
    
    style N fill:#ff9900,stroke:#333,stroke-width:2px
    style O fill:#ff9900,stroke:#333,stroke-width:2px
    style P fill:#ff9900,stroke:#333,stroke-width:2px
    style Q fill:#ff9900,stroke:#333,stroke-width:2px
    style R fill:#ff9900,stroke:#333,stroke-width:2px
    style S fill:#ff9900,stroke:#333,stroke-width:2px
    style T fill:#ff9900,stroke:#333,stroke-width:2px
    style U fill:#ff9900,stroke:#333,stroke-width:2px
    style V fill:#ff9900,stroke:#333,stroke-width:2px
    style W fill:#ff9900,stroke:#333,stroke-width:2px
```

## CloudWatch Metrics and Alarms

```mermaid
graph TD
    subgraph "System Metrics"
        A[CPU Utilization] --> B[Memory Usage]
        C[Disk I/O] --> D[Network Traffic]
        E[Request Rate] --> F[Error Rate]
        G[Response Time] --> H[Queue Length]
    end

    subgraph "Business Metrics"
        I[User Activity] --> J[Transaction Volume]
        K[Revenue Impact] --> L[Customer Satisfaction]
        M[Service Health] --> N[Resource Efficiency]
    end

    subgraph "Custom Metrics"
        O[Anomaly Score] --> P[Incident Count]
        Q[Resolution Time] --> R[MTTR]
        S[Prediction Accuracy] --> T[False Positive Rate]
    end

    subgraph "Alarm Thresholds"
        U[Critical: >90%] --> V[High: >80%]
        W[Medium: >70%] --> X[Low: >60%]
        Y[Custom Rules] --> Z[Composite Alarms]
    end

    style A fill:#ff9900,stroke:#333,stroke-width:2px
    style B fill:#ff9900,stroke:#333,stroke-width:2px
    style C fill:#ff9900,stroke:#333,stroke-width:2px
    style D fill:#ff9900,stroke:#333,stroke-width:2px
```

## EventBridge Rules and Patterns

```mermaid
graph TD
    subgraph "Scheduled Events"
        A[Daily Health Check] --> B[Weekly Analysis]
        C[Monthly Report] --> D[Quarterly Review]
        E[Custom Schedules] --> F[Recurring Tasks]
    end

    subgraph "Event Patterns"
        G[CloudWatch Alarms] --> H[API Gateway Events]
        I[S3 Bucket Events] --> J[DynamoDB Streams]
        K[Custom Events] --> L[Cross-Account Events]
    end

    subgraph "Rule Actions"
        M[Step Functions] --> N[Lambda Functions]
        O[SNS Topics] --> P[SQS Queues]
        Q[EventBridge API] --> R[Custom Targets]
    end

    style A fill:#ff9900,stroke:#333,stroke-width:2px
    style B fill:#ff9900,stroke:#333,stroke-width:2px
    style C fill:#ff9900,stroke:#333,stroke-width:2px
    style D fill:#ff9900,stroke:#333,stroke-width:2px
```

## Lambda Function Interactions

```mermaid
graph TD
    subgraph "Anomaly Detection"
        A[Collect Metrics] --> B[Preprocess Data]
        B --> C[Apply ML Models]
        C --> D[Calculate Scores]
        D --> E[Generate Alerts]
    end

    subgraph "Incident Management"
        F[Create Incident] --> G[Assign Priority]
        G --> H[Notify Teams]
        H --> I[Track Status]
        I --> J[Update Records]
    end

    subgraph "Resolution Process"
        K[Analyze Root Cause] --> L[Generate Plan]
        L --> M[Execute Actions]
        M --> N[Verify Results]
        N --> O[Document Learnings]
    end

    style A fill:#ff9900,stroke:#333,stroke-width:2px
    style B fill:#ff9900,stroke:#333,stroke-width:2px
    style C fill:#ff9900,stroke:#333,stroke-width:2px
    style D fill:#ff9900,stroke:#333,stroke-width:2px
```

## Monitoring and Alerting Flow

```mermaid
graph TD
    subgraph "Data Collection"
        A[System Metrics] --> B[Application Logs]
        C[User Activity] --> D[Business Metrics]
        E[Custom Data] --> F[External Sources]
    end

    subgraph "Analysis Pipeline"
        G[Data Processing] --> H[Anomaly Detection]
        I[Pattern Recognition] --> J[Trend Analysis]
        K[Predictive Models] --> L[Risk Assessment]
    end

    subgraph "Alert Management"
        M[Alert Generation] --> N[Severity Classification]
        O[Alert Routing] --> P[Notification Channels]
        Q[Alert Tracking] --> R[Resolution Monitoring]
    end

    subgraph "Response Actions"
        S[Automated Actions] --> T[Manual Interventions]
        U[Escalation Paths] --> V[Resolution Workflows]
        W[Post-Mortem] --> X[Knowledge Base]
    end

    style A fill:#ff9900,stroke:#333,stroke-width:2px
    style B fill:#ff9900,stroke:#333,stroke-width:2px
    style C fill:#ff9900,stroke:#333,stroke-width:2px
    style D fill:#ff9900,stroke:#333,stroke-width:2px
```

## Auto-Remediation with AWS SSM

```mermaid
graph TD
    subgraph "Incident Detection"
        A[Anomaly Detection] --> B[Incident Creation]
        B --> C[Severity Assessment]
        C --> D[Resource Identification]
    end

    subgraph "Remediation Planning"
        E[Action Selection] --> F[Risk Assessment]
        F --> G[Approval Flow]
        G --> H[SSM Document Selection]
    end

    subgraph "Execution"
        I[Pre-Remediation Check] --> J[Execute Action]
        J --> K[Post-Remediation Check]
        K --> L[Status Update]
    end

    subgraph "Verification"
        M[Metrics Analysis] --> N[Health Check]
        N --> O[Incident Resolution]
        O --> P[Documentation]
    end

    style A fill:#ff9900,stroke:#333,stroke-width:2px
    style B fill:#ff9900,stroke:#333,stroke-width:2px
    style C fill:#ff9900,stroke:#333,stroke-width:2px
    style D fill:#ff9900,stroke:#333,stroke-width:2px
```

### Auto-Remediation Features

- **Automated Actions**:
  - Instance Restart
  - Auto Scaling Group Scale Up/Down
  - RDS Backup and Recovery
  - S3 Cleanup
  - Custom Remediation Actions

- **Safety Measures**:
  - Pre and Post Remediation Checks
  - Risk Assessment
  - Approval Workflows
  - Rollback Capabilities

- **Integration**:
  - AWS Systems Manager Documents
  - CloudWatch Metrics
  - SNS Notifications
  - DynamoDB Status Tracking

### Setup Instructions

1. Install Ansible and required collections:
   ```bash
   pip install ansible
   ansible-galaxy collection install -r ansible/requirements.yml
   ```

2. Configure AWS credentials:
   ```bash
   aws configure
   ```

3. Create SSM Document:
   ```bash
   aws ssm create-document \
     --content file://ansible/ssm_documents/remediation_document.json \
     --name "AIOpsGuardian-Remediation" \
     --document-type "Command" \
     --document-format "JSON"
   ```

4. Run remediation playbook:
   ```bash
   ansible-playbook ansible/playbooks/auto_remediation.yml \
     -e "incident_id=INC-123" \
     -e "severity=HIGH" \
     -e "resource_id=i-1234567890abcdef0" \
     -e "resource_type=EC2" \
     -e "remediation_action=RESTART"
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