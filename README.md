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

## Table of Contents

1. [System Architecture](#system-architecture)
2. [Deployment Architecture](#deployment-architecture)
3. [Component Interaction](#component-interaction)
4. [Infrastructure Components](#infrastructure-components)
5. [GitOps Workflow](#gitops-workflow-with-argocd)
6. [Helm Chart Structure](#helm-chart-structure)
7. [Anomaly Detection](#anomaly-detection-flow)
8. [Step Functions Workflow](#step-functions-workflow)
9. [AWS Step Functions Integration](#aws-step-functions-integration)
10. [CloudWatch Metrics](#cloudwatch-metrics-and-alarms)
11. [EventBridge Rules](#eventbridge-rules-and-patterns)
12. [Lambda Functions](#lambda-function-interactions)
13. [Monitoring Flow](#monitoring-and-alerting-flow)
14. [Auto-Remediation](#auto-remediation-with-ansible-and-aws-ssm)
15. [Features](#features)
16. [Vector Search](#vector-search-for-incident-similarity)
17. [Project Structure](#project-structure)
18. [Prerequisites](#prerequisites)
19. [Setup Instructions](#setup-instructions)
20. [Development](#development)
21. [License](#license)

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

## Auto-Remediation with Ansible and AWS SSM

```mermaid
graph TD
    subgraph "Ansible Control Node"
        A[Ansible Playbook] --> B[SSM Document Execution]
        B --> C[Status Tracking]
        C --> D[Notification System]
    end

    subgraph "AWS SSM"
        E[SSM Document] --> F[Command Execution]
        F --> G[Parameter Management]
        G --> H[Output Collection]
    end

    subgraph "Resource Management"
        I[EC2 Instances] --> J[Auto Scaling Groups]
        K[RDS Databases] --> L[S3 Buckets]
        M[Lambda Functions] --> N[API Gateway]
    end

    subgraph "Monitoring & Feedback"
        O[CloudWatch Metrics] --> P[Log Collection]
        Q[Status Updates] --> R[Incident Tracking]
        S[Health Checks] --> T[Verification]
    end

    A --> E
    E --> I
    E --> K
    E --> M
    F --> O
    H --> Q
    T --> C

    style A fill:#ff9900,stroke:#333,stroke-width:2px
    style B fill:#ff9900,stroke:#333,stroke-width:2px
    style C fill:#ff9900,stroke:#333,stroke-width:2px
    style D fill:#ff9900,stroke:#333,stroke-width:2px
```

### Ansible Integration Features

- **Playbook Management**:
  - Dynamic inventory management
  - Role-based execution
  - Variable templating
  - Conditional execution
  - Error handling and retries

- **SSM Document Integration**:
  - Document versioning
  - Parameter validation
  - Output collection
  - Status tracking
  - Error handling

- **Resource Management**:
  - Multi-resource support
  - State management
  - Dependency handling
  - Rollback capabilities
  - Health verification

### Ansible Playbook Structure

```yaml
# Example playbook structure
---
- name: Auto-Remediation Playbook
  hosts: localhost
  gather_facts: false
  vars:
    aws_region: "{{ aws_region | default('us-west-2') }}"
    incident_id: "{{ incident_id }}"
    severity: "{{ severity }}"
    resource_id: "{{ resource_id }}"
    resource_type: "{{ resource_type }}"
    remediation_action: "{{ remediation_action }}"
    ssm_document_name: "{{ ssm_document_name | default('AIOpsGuardian-Remediation') }}"

  tasks:
    - name: Get AWS SSM Document
      amazon.aws.ssm_document_info:
        name: "{{ ssm_document_name }}"
        region: "{{ aws_region }}"
      register: ssm_doc

    - name: Execute SSM Document
      amazon.aws.ssm_document_execution:
        document_name: "{{ ssm_document_name }}"
        parameters:
          IncidentId: "{{ incident_id }}"
          Severity: "{{ severity }}"
          ResourceId: "{{ resource_id }}"
          ResourceType: "{{ resource_type }}"
          RemediationAction: "{{ remediation_action }}"
        region: "{{ aws_region }}"
      register: execution_result
      when: ssm_doc.documents is defined and ssm_doc.documents | length > 0

    - name: Update Incident Status
      amazon.aws.dynamodb_table:
        name: "AIOpsGuardian-Incidents"
        region: "{{ aws_region }}"
        operation: update_item
        key:
          IncidentId: "{{ incident_id }}"
        attributes:
          RemediationStatus: "{{ 'COMPLETED' if execution_result.status == 'SUCCESS' else 'FAILED' }}"
          RemediationResult: "{{ execution_result.output }}"
          LastUpdated: "{{ ansible_date_time.iso8601 }}"
      when: execution_result is defined

    - name: Send SNS Notification
      amazon.aws.sns_topic:
        region: "{{ aws_region }}"
        topic_arn: "arn:aws:sns:{{ aws_region }}:{{ aws_account_id }}:AIOpsGuardian-Remediation"
        message: |
          Remediation executed for incident {{ incident_id }}
          Status: {{ execution_result.status if execution_result is defined else 'FAILED' }}
          Resource: {{ resource_id }}
          Action: {{ remediation_action }}
        subject: "AIOps Guardian - Remediation {{ execution_result.status if execution_result is defined else 'FAILED' }}"
      when: execution_result is defined

    - name: Log Remediation Result
      amazon.aws.cloudwatch_log:
        region: "{{ aws_region }}"
        log_group: "/aws/aiops-guardian/remediation"
        log_stream: "{{ incident_id }}"
        message: |
          {
            "timestamp": "{{ ansible_date_time.iso8601 }}",
            "incident_id": "{{ incident_id }}",
            "resource_id": "{{ resource_id }}",
            "remediation_action": "{{ remediation_action }}",
            "status": "{{ execution_result.status if execution_result is defined else 'FAILED' }}",
            "result": "{{ execution_result.output if execution_result is defined else 'No execution result' }}"
          }
      when: execution_result is defined
```

### Setup and Configuration

1. **Install Ansible and AWS Collections**:
   ```bash
   # Install Ansible
   pip install ansible

   # Install required collections
   ansible-galaxy collection install -r ansible/requirements.yml
   ```

2. **Configure AWS Credentials**:
   ```bash
   # Configure AWS CLI
   aws configure

   # Or set environment variables
   export AWS_ACCESS_KEY_ID="your_access_key"
   export AWS_SECRET_ACCESS_KEY="your_secret_key"
   export AWS_DEFAULT_REGION="us-west-2"
   ```

3. **Create SSM Document**:
   ```bash
   # Create the SSM document
   aws ssm create-document \
     --content file://ansible/ssm_documents/remediation_document.json \
     --name "AIOpsGuardian-Remediation" \
     --document-type "Command" \
     --document-format "JSON"
   ```

4. **Run Remediation Playbook**:
   ```bash
   # Basic execution
   ansible-playbook ansible/playbooks/auto_remediation.yml \
     -e "incident_id=INC-123" \
     -e "severity=HIGH" \
     -e "resource_id=i-1234567890abcdef0" \
     -e "resource_type=EC2" \
     -e "remediation_action=RESTART"

   # With additional variables
   ansible-playbook ansible/playbooks/auto_remediation.yml \
     -e "incident_id=INC-123" \
     -e "severity=HIGH" \
     -e "resource_id=i-1234567890abcdef0" \
     -e "resource_type=EC2" \
     -e "remediation_action=RESTART" \
     -e "aws_region=us-west-2" \
     -e "ssm_document_name=AIOpsGuardian-Remediation-v2"
   ```

### Best Practices

1. **Playbook Organization**:
   - Use roles for modularity
   - Implement proper error handling
   - Include documentation
   - Use variables for flexibility

2. **SSM Document Management**:
   - Version control documents
   - Implement parameter validation
   - Include proper error handling
   - Document all actions

3. **Security Considerations**:
   - Use IAM roles
   - Implement least privilege
   - Secure sensitive data
   - Audit all actions

4. **Monitoring and Logging**:
   - Track all executions
   - Monitor performance
   - Log all actions
   - Implement alerts

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

## Vector Search for Incident Similarity

The AIOps Guardian system implements advanced vector search capabilities using both traditional embeddings and BERT-based embeddings for incident similarity search. This dual-embedding approach provides enhanced semantic understanding and improved search accuracy.

> **Integration Points**:
> - Works with [Anomaly Detection](#anomaly-detection-flow) for incident pattern matching
> - Integrates with [Knowledge Base](#component-interaction) for historical data
> - Supports [Auto-Remediation](#auto-remediation-with-ansible-and-aws-ssm) through similar incident resolution
> - Provides metrics for [CloudWatch Monitoring](#cloudwatch-metrics-and-alarms)

### Architecture

```mermaid
graph TD
    subgraph "Data Sources"
        A1[CloudWatch Logs] --> A[Incident Data]
        A2[CloudWatch Metrics] --> A
        A3[System Events] --> A
        A4[User Reports] --> A
    end

    subgraph "Processing Pipeline"
        B[Text Preprocessing]
        B1[Tokenization] --> B
        B2[Cleaning] --> B
        B3[Normalization] --> B
    end

    subgraph "Embedding Generation"
        C[Traditional Embeddings]
        D[BERT Embeddings]
        D1[BERT-base] --> D
        D2[BERT-large] --> D
        D3[RoBERTa] --> D
        D4[DistilBERT] --> D
    end

    subgraph "Vector Storage"
        E[FAISS Index]
        F[BERT FAISS Index]
        G[DynamoDB]
    end

    subgraph "Search Interface"
        H[Query Processing]
        I[Traditional Search]
        J[BERT Search]
        K[Results Aggregation]
        L[Similar Incidents]
    end

    subgraph "Integration Layer"
        O[Anomaly Detection]
        P[Knowledge Base]
        Q[Auto-Remediation]
        R[CloudWatch]
        S[Step Functions]
        T[Lambda Functions]
    end

    A --> B
    B --> C
    B --> D
    C --> E
    D --> F
    E --> G
    F --> G
    G --> H
    H --> I
    H --> J
    I --> K
    J --> K
    K --> L

    O --> A
    P --> A
    Q --> L
    R --> K
    S --> L
    T --> L

    style A fill:#ff9900,stroke:#333,stroke-width:2px
    style B fill:#ff9900,stroke:#333,stroke-width:2px
    style C fill:#ff9900,stroke:#333,stroke-width:2px
    style D fill:#ff9900,stroke:#333,stroke-width:2px
    style E fill:#ff9900,stroke:#333,stroke-width:2px
    style F fill:#ff9900,stroke:#333,stroke-width:2px
    style G fill:#ff9900,stroke:#333,stroke-width:2px
    style H fill:#ff9900,stroke:#333,stroke-width:2px
    style I fill:#ff9900,stroke:#333,stroke-width:2px
    style J fill:#ff9900,stroke:#333,stroke-width:2px
    style K fill:#ff9900,stroke:#333,stroke-width:2px
    style L fill:#ff9900,stroke:#333,stroke-width:2px
```

### Integration Examples

1. **Anomaly Detection Integration**
```python
# Search for similar historical anomalies
POST /api/v1/vector-search/search
{
    "query": "CPU utilization spike in production",
    "k": 5,
    "use_bert": true,
    "model_type": "BERT_LARGE",
    "filter": {
        "type": "ANOMALY",
        "severity": "HIGH",
        "time_range": "LAST_30_DAYS"
    },
    "include_metrics": true,
    "include_logs": true
}
```

2. **Knowledge Base Integration**
```python
# Search knowledge base for similar incidents
POST /api/v1/vector-search/search
{
    "query": "database connection pool exhaustion",
    "k": 5,
    "use_bert": true,
    "model_type": "ROBERTA",
    "source": "KNOWLEDGE_BASE",
    "include_solutions": true,
    "include_playbooks": true
}
```

3. **Auto-Remediation Integration**
```python
# Find similar resolved incidents for auto-remediation
POST /api/v1/vector-search/search
{
    "query": "high memory usage in production database",
    "k": 5,
    "use_bert": true,
    "model_type": "BERT_LARGE",
    "filter": {
        "status": "RESOLVED",
        "severity": "HIGH",
        "has_remediation": true
    },
    "include_remediation_steps": true,
    "include_verification": true
}
```

4. **Step Functions Integration**
```python
# Search for similar incidents in workflow
POST /api/v1/vector-search/search
{
    "query": "service degradation in user-facing API",
    "k": 5,
    "use_bert": true,
    "model_type": "BERT_LARGE",
    "workflow_id": "INC-123",
    "include_workflow_state": true,
    "include_actions_taken": true
}
```

5. **Lambda Function Integration**
```python
# Search for similar incidents in Lambda context
POST /api/v1/vector-search/search
{
    "query": "error rate spike in payment service",
    "k": 5,
    "use_bert": true,
    "model_type": "BERT_LARGE",
    "lambda_context": {
        "function_name": "payment-processor",
        "error_type": "TimeoutException",
        "region": "us-west-2"
    },
    "include_error_patterns": true,
    "include_stack_traces": true
}
```

6. **CloudWatch Integration**
```python
# Search incidents with metric correlation
POST /api/v1/vector-search/search
{
    "query": "high latency in API endpoints",
    "k": 5,
    "use_bert": true,
    "model_type": "BERT_LARGE",
    "metrics": {
        "latency": ">500ms",
        "error_rate": ">1%",
        "time_range": "LAST_HOUR"
    },
    "include_metric_graphs": true,
    "include_log_insights": true
}
```

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
