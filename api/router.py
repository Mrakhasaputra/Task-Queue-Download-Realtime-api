from fastapi import APIRouter
from api.endpoints.task_queue import router as task_queue_router

router = APIRouter()

router.include_router(task_queue_router, prefix="/task-queue", tags=["Task Queue"])