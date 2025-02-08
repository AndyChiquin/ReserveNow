from fastapi import APIRouter, HTTPException
from app.database.database import feedbacks_collection
from bson import ObjectId

router = APIRouter()

@router.get("/{feedback_id}")
async def get_feedback(feedback_id: str):
    feedback = await feedbacks_collection.find_one({"_id": ObjectId(feedback_id)})
    if not feedback:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return feedback

@router.get("/")
async def list_feedbacks():
    feedbacks = await feedbacks_collection.find().to_list(100)
    return feedbacks
