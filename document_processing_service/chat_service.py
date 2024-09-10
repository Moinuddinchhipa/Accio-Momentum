# chat_service.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from collections import defaultdict

app = FastAPI()

class ChatMessage(BaseModel):
    thread_id: str
    user_message: str

class StartChat(BaseModel):
    asset_id: str

class ChatHistoryResponse(BaseModel):
    messages: list

chat_threads = defaultdict(list)

@app.post("/api/chat/start")
async def start_chat(start_chat: StartChat):
    thread_id = str(len(chat_threads) + 1)
    chat_threads[thread_id].append({"role": "system", "content": f"Chat started for asset ID: {start_chat.asset_id}"})
    return {"thread_id": thread_id}

@app.post("/api/chat/message")
async def send_message(chat_message: ChatMessage):
    if chat_message.thread_id not in chat_threads:
        raise HTTPException(status_code=404, detail="Chat thread not found")

    # Simulated agent response (should integrate with LangChain)
    agent_response = f"Agent response to: {chat_message.user_message}"
    chat_threads[chat_message.thread_id].append({"role": "user", "content": chat_message.user_message})
    chat_threads[chat_message.thread_id].append({"role": "agent", "content": agent_response})

    return {"response": agent_response}

@app.get("/api/chat/history")
async def get_chat_history(thread_id: str):
    if thread_id not in chat_threads:
        raise HTTPException(status_code=404, detail="Chat thread not found")

    return ChatHistoryResponse(messages=chat_threads[thread_id])
