from fastapi import FastAPI
from app.domain.read.read import router as read_router

app = FastAPI(title="Read Service", description="Handles table reading operations")

app.include_router(read_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
