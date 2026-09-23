from pydantic import BaseModel, field_validator


class AnalyzeRequest(BaseModel):
    image_url: str
    model_name: str = "mock"

    @field_validator("image_url")
    def must_not_be_empty(cls, image_url):
        if image_url == "":
            raise ValueError("image_url cannot be empty")
        return image_url


class JobResponse(BaseModel):
    job_id: str
    status: str
    progress: int = 0
