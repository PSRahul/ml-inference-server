import uuid

from fastapi import FastAPI, HTTPException

from src.ml_inference_server.models import AnalyzeRequest, JobResponse

app = FastAPI()

jobs: dict[str, JobResponse] = {}


@app.get(path="/health")
async def get_health():
    return {"status": "ok"}


@app.post(path="/analyze", response_model=JobResponse)
async def post_analyze(analyze_request: AnalyzeRequest):

    response = JobResponse(
        job_id=str(uuid.uuid4()),
        status="pending",
    )
    jobs[response.job_id] = response
    return response


@app.get(path="/jobs/{job_id}", response_model=JobResponse)
async def get_jobs(job_id: str):
    if job_id in jobs:
        return jobs[job_id]
    else:
        raise HTTPException(status_code=404, detail="Job ID not found")
