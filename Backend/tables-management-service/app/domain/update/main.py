from fastapi import FastAPI
from app.domain.update.update import router as update_router

app = FastAPI(title="Update Service", description="Handles table update operations")

app.include_router(update_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8003)
