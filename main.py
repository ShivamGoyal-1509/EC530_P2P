from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import redis

app = FastAPI()
r = redis.Redis(host="localhost", port=6379, decode_responses=True)

class Message(BaseModel):
    sender: str
    recipient: str
    content: str

@app.post("/send")
def send_message(msg: Message):
    channel = f"user:{msg.recipient}"
    message_data = f"{msg.sender}: {msg.content}"
    r.publish(channel, message_data)
    return {"status": "Message sent", "to": msg.recipient}