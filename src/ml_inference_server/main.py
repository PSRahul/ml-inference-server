from fastapi import FastAPI

from src.ml_inference_server.models import AnalyzeResult, JobResponse

_, _ = AnalyzeResult, JobResponse

app = FastAPI()


@app.get(path="/health")
async def get_health():
    return {"status": "ok"}
