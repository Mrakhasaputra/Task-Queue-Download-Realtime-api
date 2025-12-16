import asyncio
import os
from database import SessionLocal
from models.task import Task
from websocket_manager import manager

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)


async def worker():
    print("Worker started...")
    while True:
        db = SessionLocal()
        try:
            task = db.query(Task).filter(Task.status == "waiting").first()
            if not task:
                await asyncio.sleep(2)
                continue

            task.status = "progress"
            db.commit()
            await manager.broadcast({
                "event": "task_update",
                "data": {
                    "id": task.id,
                    "title": task.title,
                    "status": task.status,
                    "file_path": task.file_path
                }
            })

            await asyncio.sleep(5)  # simulasi download

            task.file_path = f"{DOWNLOAD_DIR}/task_{task.id}.txt"
            with open(task.file_path, "w") as f:
                f.write(f"Downloaded {task.title}")

            task.status = "done"
            db.commit()
            await manager.broadcast({
                "event": "task_update",
                "data": {
                    "id": task.id,
                    "title": task.title,
                    "status": task.status,
                    "file_path": task.file_path
                }
            })

        except Exception as e:
            db.rollback()
            print("Worker error:", e)
        finally:
            db.close()

        await asyncio.sleep(3)