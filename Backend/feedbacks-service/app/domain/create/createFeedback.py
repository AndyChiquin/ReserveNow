from fastapi import APIRouter, HTTPException
from app.database.database import feedbacks_collection
from app.utils.validation import Feedback
from datetime import datetime

router = APIRouter()

@router.post("/")
async def create_feedback(feedback: Feedback):
    new_feedback = feedback.dict()
    new_feedback["created_at"] = datetime.utcnow()
    new_feedback["updated_at"] = datetime.utcnow()
    
    result = await feedbacks_collection.insert_one(new_feedback)
    return {"id": str(result.inserted_id), "message": "Feedback created successfully"}
