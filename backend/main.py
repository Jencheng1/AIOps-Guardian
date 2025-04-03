from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import boto3
import json
import logging
from datetime import datetime
from opentelemetry import trace
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentation

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize AWS Bedrock client
bedrock = boto3.client('bedrock-runtime')

app = FastAPI(title="SRE Copilot API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize OpenTelemetry
FastAPIInstrumentation.instrument(app)

class Incident(BaseModel):
    id: str
    title: str
    description: str
    severity: str
    status: str
    timestamp: datetime
    metrics: Optional[List[dict]] = None
    logs: Optional[List[dict]] = None
    dashboard_data: Optional[dict] = None

class AnalysisRequest(BaseModel):
    incident_id: str
    data_type: str  # "logs", "metrics", or "dashboard"
    data: dict

class AgentResponse(BaseModel):
    agent_id: str
    analysis: str
    confidence: float
    recommendations: List[str]

@app.post("/api/incidents")
async def create_incident(incident: Incident):
    try:
        # Store incident in database (implementation needed)
        return {"message": "Incident created successfully", "incident_id": incident.id}
    except Exception as e:
        logger.error(f"Error creating incident: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/analyze")
async def analyze_incident(request: AnalysisRequest):
    try:
        # Prepare prompt for AWS Bedrock
        prompt = f"""
        Analyze the following {request.data_type} data for incident {request.incident_id}:
        {json.dumps(request.data, indent=2)}
        
        Please provide:
        1. Root cause analysis
        2. Impact assessment
        3. Recommended actions
        """
        
        # Call AWS Bedrock
        response = bedrock.invoke_model(
            modelId='anthropic.claude-v2',
            body=json.dumps({
                "prompt": prompt,
                "max_tokens": 1000,
                "temperature": 0.7
            })
        )
        
        # Parse response
        response_body = json.loads(response['body'].read())
        analysis = response_body['completion']
        
        return {
            "incident_id": request.incident_id,
            "analysis": analysis,
            "timestamp": datetime.utcnow()
        }
    except Exception as e:
        logger.error(f"Error analyzing incident: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/incidents/{incident_id}")
async def get_incident(incident_id: str):
    try:
        # Retrieve incident from database (implementation needed)
        return {"message": f"Retrieved incident {incident_id}"}
    except Exception as e:
        logger.error(f"Error retrieving incident: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/metrics")
async def get_metrics():
    try:
        # Implement metrics collection
        return {"message": "Metrics endpoint"}
    except Exception as e:
        logger.error(f"Error retrieving metrics: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 