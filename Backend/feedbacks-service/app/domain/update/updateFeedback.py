from fastapi import APIRouter, HTTPException
from app.database.database import feedbacks_collection
from app.utils.validation import FeedbackUpdate
from bson import ObjectId
from datetime import datetime

router = APIRouter()

@router.put("/{feedback_id}")
async def update_feedback(feedback_id: str, feedback: FeedbackUpdate):
    update_data = {k: v for k, v in feedback.dict().items() if v is not None}
    update_data["updated_at"] = datetime.utcnow()
    
    result = await feedbacks_collection.update_one({"_id": ObjectId(feedback_id)}, {"$set": update_data})
    
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Feedback not found")
    
    return {"message": "Feedback updated successfully"}
