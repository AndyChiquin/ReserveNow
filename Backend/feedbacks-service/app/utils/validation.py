from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Feedback(BaseModel):
    user_id: str
    reservation_id: str
    comment: str
    rating: int
    created_at: Optional[datetime] = datetime.utcnow()
    updated_at: Optional[datetime] = datetime.utcnow()

class FeedbackUpdate(BaseModel):
    comment: Optional[str]
    rating: Optional[int]
    updated_at: datetime = datetime.utcnow()
