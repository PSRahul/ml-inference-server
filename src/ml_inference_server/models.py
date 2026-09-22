from pydantic import BaseModel


class AnalyzeRequest(BaseModel):
    image_url: str
    model_name: str = "mock"


class JobResponse(BaseModel):
    job_id: str
    status: str
    progress: int = 0
