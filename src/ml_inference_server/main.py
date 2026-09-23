import asyncio
import uuid

from fastapi import BackgroundTasks, FastAPI, HTTPException

from src.ml_inference_server.models import AnalyzeRequest, JobResponse

app = FastAPI()

jobs: dict[str, JobResponse] = {}


async def run_inference(job_response: JobResponse):
    job_response.status = "running"
    job_response.progress = 25
    await asyncio.sleep(5)
    job_response.status = "completed"
    job_response.progress = 100


@app.get(path="/health")
async def get_health():
    return {"status": "ok"}


@app.post(
    path="/analyze",
    response_model=JobResponse,
)
async def post_analyze(
    analyze_request: AnalyzeRequest, background_tasks: BackgroundTasks
):

    response = JobResponse(
        job_id=str(uuid.uuid4()),
        status="pending",
    )
    background_tasks.add_task(run_inference, response)
    jobs[response.job_id] = response
    return response


@app.get(path="/jobs/{job_id}", response_model=JobResponse)
async def get_jobs(job_id: str):
    if job_id in jobs:
        return jobs[job_id]
    else:
        raise HTTPException(status_code=404, detail="Job ID not found")
