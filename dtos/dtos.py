# buatkan dots
from pydantic import BaseModel

class TaskResponse(BaseModel):
    id: int
    title: str
    status: str

    model_config = {
        "from_attributes": True
    }

class TaskCreateRequest(BaseModel):
    title: str