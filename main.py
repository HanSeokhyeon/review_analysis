from fastapi import FastAPI, Body
from pydantic import BaseModel

from ch2.inference import inference_json


app = FastAPI()


class RequestBody(BaseModel):
    review: str


@app.post("/evaluate")
async def evaluate_review(body: RequestBody = Body()):
    return inference_json(body)
