import logging
from fastapi import FastAPI
from app.domain.create.createFeedback import router as create_router
from app.domain.read.readFeedback import router as read_router
from app.domain.update.updateFeedback import router as update_router
from app.domain.delete.deleteFeedback import router as delete_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.include_router(create_router, prefix="/feedbacks", tags=["Create Feedback"])
app.include_router(read_router, prefix="/feedbacks", tags=["Read Feedback"])
app.include_router(update_router, prefix="/feedbacks", tags=["Update Feedback"])
app.include_router(delete_router, prefix="/feedbacks", tags=["Delete Feedback"])

@app.get("/")
async def root():
    return {"message": "Feedbacks Service is running"}

logger.info("🚀 FastAPI is running at http://127.0.0.1:8000 🚀")
