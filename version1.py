from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

calls = {}


class Call(BaseModel):
    call_id: str
    status: str
    duration_secs: int


@app.post("/call-ended")
def call_ended(call: Call):
    if call.call_id not in calls:
        calls[call.call_id] = call

    return {"message": "Call stored successfully"}


@app.get("/calls/{call_id}")
def get_call(call_id: str):
    if call_id not in calls:
        raise HTTPException(status_code=404, detail="Call not found")

    return calls[call_id]