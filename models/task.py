from sqlalchemy import Column, Integer, String, DateTime, Enum
from datetime import datetime
from database import Base

class Task(Base):
    __tablename__ = "task_queue"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    status = Column(Enum("waiting", "progress", "done"), index=True)
    file_path = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)