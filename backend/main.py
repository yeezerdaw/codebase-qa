from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.core.processor import RepoProcessor

app = FastAPI()
processor = RepoProcessor()


class RepoRequest(BaseModel):
    repo_url: str


@app.post("/process-repo")
async def process_repo(request: RepoRequest):  # Accept repo_url from the request body
    try:
        path = processor.clone_repo(request.repo_url)
        return {"status": "success", "path": path}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
