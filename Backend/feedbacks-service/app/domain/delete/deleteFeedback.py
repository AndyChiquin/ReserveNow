from fastapi import APIRouter, HTTPException
from app.database.database import feedbacks_collection
from bson import ObjectId

router = APIRouter()

@router.delete("/{feedback_id}")
async def delete_feedback(feedback_id: str):
    result = await feedbacks_collection.delete_one({"_id": ObjectId(feedback_id)})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Feedback not found")
    
    return {"message": "Feedback deleted successfully"}
