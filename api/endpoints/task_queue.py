from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from sqlalchemy.orm import Session
from database import get_db
from websocket_manager import manager
from dtos.dtos import TaskResponse, TaskCreateRequest
from services.task_queue import TaskService
from typing import List

router = APIRouter()

@router.post("/tasks/", response_model=TaskResponse)
def create_task(task_request: TaskCreateRequest, db: Session = Depends(get_db)):
    service = TaskService(db)
    task = service.create_task(task_request)
    return task

@router.get("/tasks/", response_model=List[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    service = TaskService(db)
    tasks = service.get_tasks()
    return tasks

@router.websocket("/ws/tasks")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        await websocket.send_json({"event": "connected"})
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)